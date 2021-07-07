""" 
Implmentation of a HashTable in Python.
@author HELEGAH RAYNARD DODZI
@email dodzireynard@gmail.com
@date 06.05.2021
"""
from collections import namedtuple
from typing import Any

Element = namedtuple("Element", "key, value")


class HashTable:
    """HasthTable stores key and value pairs with dynamic resizing.

    Creating a new HashTable
            hash_table = HashTable()

        New HashTable with a specified initial size.
            hash_table = HashTable(65599)

        Inserting an item
            hash_table[key] = value

        Retrieving an item
            hash_table.get(key)

        Deleting an item
            hash_table.delete(key)

        Getting the size of the hashtable
            len(hash_table)
    """
    def __init__(self,
                 init_size: int = 8,
                 load_factor: float = 0.75,
                 reduce_factor: float = 0.65,
                 increment: float = 2.0,
                 decrement: float = 0.6):
        self._slot = [None for _ in range(init_size)]
        self._size = 0
        self._init_size = init_size
        self._load_factor = load_factor
        self._reduce_factor = reduce_factor
        self._increment = increment
        self._decrement = decrement

    def _get_index(self, key):
        return hash(key) % len(self._slot)

    def _resize(self, factor: float) -> None:
        """Resizes the the available slots.
        Args:
            factor: The factor by which to resize the slots. factor < 1 reduces the slot
            and factor > 1 increases the slots.
        """
        self._size = 0
        old_table = self._slot.copy()
        new_size = int(len(self._slot) * factor) if self._init_size < int(
            len(self._slot) * factor) else self._init_size
        self._slot = [None for _ in range(new_size)]

        for entry in old_table:
            if entry:
                for key, value in entry:
                    self[key] = value

    def __setitem__(self, key, value):
        index = self._get_index(key)
        element = Element(key, value)

        if self._slot[index]:
            for sub_index, item in enumerate(self._slot[index]):
                # Key already exists, override the value by replacing the element at that position.
                if item.key == key:
                    self._slot[index][sub_index] = element
                    return
            # The key does not already exist.
            self._slot[index].append(element)
        else:
            self._slot[index] = [element]
        self._size += 1

        load_factor = self._size / len(self._slot)
        if load_factor > self._load_factor:
            self._resize(self._increment)

    def __delitem__(self, key):
        index = self._get_index(key)
        if self._slot[index]:
            for sub_index, item in enumerate(self._slot[index]):
                if item[0] == key:
                    del self._slot[index][sub_index]
                    self._size -= 1
        load_factor = self._size / len(self._slot)
        if load_factor < self._reduce_factor:
            self._resize(self._decrement)

    def __getitem__(self, key):
        index = self._get_index(key)
        if self._slot[index]:
            for item in self._slot[index]:
                if item[0] == key:
                    return item[1]
        return None

    def insert(self, key: Any, value: Any):
        """Inserts an item with the speficied key."""
        self[key] = value

    def get(self, key: Any) -> Any:
        """Retrieves an item with the speficied key."""
        return self[key]

    def delete(self, key: Any) -> None:
        """Deletes an item with the speficied key."""
        del self[key]

    def get_slot_size(self) -> int:
        """Returns size of the slot"""
        return len(self._slot)

    def __len__(self):
        return self._size
