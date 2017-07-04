import unittest2 as unittest
from str_similarity import similarity_str
from similarity import similarity_check

class test_similarity_str(unittest.TestCase):

    def test_similarity(self):
        self.assertTrue(similarity_str("Hello World", "Hello World"), msg=r"both strings are 100% similar")

    def test_false_similarity(self):
        self.assertFalse(similarity_str("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_false_similarity(self):
        self.assertEqual(similarity_str("world", "smug"), 0.0, msg='should be equal to 0.0')

    def test_NotEqual_similarity(self):
        self.assertNotEqual(similarity_str("Hel lo", "World "), 0.0, msg='Hel lo" and "World" are not similar')

    def test_invalid_str(self):
        self.assertFalse(similarity_str("world11", "hello"), msg="Should return False input")

    def test_invalid_str2(self):
        self.assertFalse(similarity_str("world", "hello1"), msg="Should return False input")

    def test_invalid_str3(self):
        self.assertFalse(similarity_str("world1", "hello1"), msg="Should return False input")

    def test_valid_str_sapce(self):
        self.assertTrue(similarity_str("wor ld", "he llo"), msg="Should return True")


    def test_similarity2(self):
        self.assertTrue(similarity_check("Hello World", "Hello World"), msg=r"both strings are 100% similar")

    def test_false_similarity2(self):
        self.assertFalse(similarity_check("world", "smug"), 0.0, msg='"world" and "smug" are not similar')

    def test_false_similarity2(self):
        self.assertEqual(similarity_check("world", "smug"), 0.0, msg='should be equal to 0.0')

    def test_NotEqual_similarity2(self):
        self.assertNotEqual(similarity_check("Hel lo", "World "), 0.0, msg='Hel lo" and "World" are not similar')

    def test_invalid_str_1(self):
        self.assertFalse(similarity_check("world11", "hello"), msg="Should return False input")

    def test_invalid_str_2(self):
        self.assertFalse(similarity_check("world", "hello1"), msg="Should return False input")

    def test_invalid_str_3(self):
        self.assertFalse(similarity_check("world1", "hello1"), msg="Should return False input")

    def test_valid_str_sapce_true(self):
        self.assertTrue(similarity_check("wor ld", "he llo"), msg="Should return True")

if __name__ == '__main__':
    unittest.main()
