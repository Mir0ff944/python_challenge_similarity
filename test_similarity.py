import unittest2 as unittest
from str_similarity import similarity_str
from similarity import similarity_check

class test_similarity_str(unittest.TestCase):

    def test_similarity(self):
        self.assertTrue(similarity_str("Hello World", "Hello World"), msg=r"both strings are 100% similar")

    def test_false_similarity(self):
        self.assertFalse(similarity_str("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_false_similarity(self):
        self.assertEqual(similarity_str("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_NotEqual_similarity(self):
        self.assertNotEqual(similarity_str("Hel lo", "World "), 0.0, msg='"world" and "smug" are not similar')


    def test_similarity2(self):
        self.assertTrue(similarity_check("Hello World", "Hello World"), msg=r"both strings are 100% similar")

    def test_false_similarity2(self):
        self.assertFalse(similarity_check("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_false_similarity2(self):
        self.assertEqual(similarity_check("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_NotEqual_similarity2(self):
        self.assertNotEqual(similarity_check("Hel lo", "World "), 0.0, msg='"world" and "smug" are not similar')

if __name__ == '__main__':
    unittest.main()
