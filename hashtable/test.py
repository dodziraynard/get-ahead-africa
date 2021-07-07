import unittest
from hashtable import HashTable
from hypothesis import given, strategies as st


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    @given(st.randoms(), st.randoms())
    def test_insertion(self, key, value):
        self.hash_table[key] = value
        self.assertEqual(self.hash_table.get(key), value)
        
    def test_insert_function(self):
        self.hash_table.insert("age", 55)
        self.assertEqual(self.hash_table.get("age"), 55)

    def test_deletion(self):
        self.hash_table["age"] = 55
        self.hash_table["name"] = "John"
        self.hash_table.delete("age")
        self.assertEqual(self.hash_table.get("age"), None)

    def test_update_if_key_exists(self):
        self.hash_table["age"] = 55
        self.hash_table["age"] = 66
        self.assertEqual(self.hash_table.get("age"), 66)

    def test_size(self):
        self.hash_table["age"] = 55
        self.hash_table["name"] = "John"
        self.assertEqual(len(self.hash_table), 2)

    def test_initial_size(self):
        self.assertEqual(len(self.hash_table._slot), 8)

    def test_increment_resize(self):
        for i in range(9):
            self.hash_table[f"{i}"] = "John"
        self.assertEqual(self.hash_table.get_slot_size(), 8 * 2)

    def test_decrement_resize(self):
        for i in range(14):
            self.hash_table[f"{i}"] = "John"
        for i in range(10):
            self.hash_table.delete(f"{i}")
        self.assertEqual(self.hash_table.get_slot_size(), 8)

    def test_size_after_update(self):
        self.hash_table["age"] = 55
        self.hash_table["name"] = "John"
        self.hash_table["name"] = "John"
        self.hash_table["name"] = "John"
        self.assertEqual(len(self.hash_table), 2)


if __name__ == '__main__':
    unittest.main()