""" 
Implmentation of a HashTable in python.
@author HELEGAH RAYNARD DODZI
@email dodzireynard@gmail.com
@date 06.05.2021
"""

class HashTable:
    """ Creating a new HashTable
            hash_table = HashTable()

        New HashTable with a specified initial size.
            hash_table = HashTable(65599)

        Inserting an item
            hash_table.insert(key, value)

        Retrieving an item
            hash_table.get(key)

        Deleting an item
            hash_table.delete(key)

        Getting the size of the hashtable
            len(hash_table)

    """

    def __init__(self, size=65599):
        self.table = [None for _ in range(size)]
        self.table_size = 0

    def _get_hash(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % len(self.table)
    
    def _resize(self, factor):
        self.table_size = 0
        new_table = [None for _ in range(int(len(self.table) * factor))]
        old_table = self.table.copy()
        self.table = new_table
        for entry in old_table:
            if entry:
                for item in entry:
                    key = item[0]
                    value = item[1]
                    self.insert(key, value) 

    def insert(self, key, value):
        '''Insert a new item with key and value into the hashtable.
        '''
        index = self._get_hash(key)
        if self.table[index]:
            for item in self.table[index]:
                if item[0] == key:
                    item[1] = value
                    return
            self.table[index].append([key, value])
            self.table_size += 1
        else:
            self.table[index] = [[key, value]]
            self.table_size += 1

        load_factor = self.table_size/len(self.table)
        if load_factor > 0.75:
            self._resize(2)

    def delete(self, key):
        '''Remove an item with speficied key from the hash table.
        '''
        index = self._get_hash(key)
        if self.table[index]:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    self.table[index].remove(item)
                    self.table_size -= 1
        load_factor = self.table_size/len(self.table)
        if load_factor < 0.5:
            self._resize(0.6)

    def get(self, key):
        '''Retrieve an item with the speficied key.
        '''
        index = self._get_hash(key)
        if self.table[index]:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def __len__(self):
        return self.table_size