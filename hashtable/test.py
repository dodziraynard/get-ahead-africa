import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def test_insertion(self):
        self.hash_table.insert("age", 55)
        self.assertEqual(self.hash_table.get("age"), 55)
    
    def test_deletion(self):
        self.hash_table.insert("age", 55)
        self.hash_table.insert("name", "John")
        self.hash_table.delete("age")
        self.assertEqual(self.hash_table.get("age"), None)
    
    def test_update_if_key_exists(self):
        self.hash_table.insert("age", 55)
        self.hash_table.insert("age", 66)
        self.assertEqual(self.hash_table.get("age"), 66)

    def test_size(self):
        self.hash_table.insert("age", 55)
        self.hash_table.insert("name", "John")
        self.assertEqual(len(self.hash_table), 2)
    
    def test_size_after_update(self):
        self.hash_table.insert("age", 55)
        self.hash_table.insert("name", "John")
        self.hash_table.insert("name", "John")
        self.hash_table.insert("name", "John")
        self.assertEqual(len(self.hash_table), 2)

if __name__ == '__main__':
    unittest.main()