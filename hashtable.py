""" 
Implmentation of a HashTable in python.
@author HELEGAH RAYNARD DODZI
@date 06.05.2021
"""

class HashTable:
    table = [None for _ in range(65599)]
    table_size = 0

    def _get_hash(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % len(self.table)
    
    def _resize(self, factor):
        print("ra", int(len(self.table) * factor))
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
        index = self._get_hash(key)
        if self.table[index]:
            for item in self.table[index]:
                if item[0] == key:
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
        index = self._get_hash(key)
        if self.table[index]:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None