from rc4 import *
import unittest

class TestRC4(unittest.TestCase):
    def test1(self):
        plain_text = "Plaintext"
        key = "Key"
        self.assertEqual(encrypt(plain_text, key), "BBF316E8D940AF0AD3")

    def test2(self):
        plain_text = "pedia"
        key = "Wiki"
        self.assertEqual(encrypt(plain_text, key), "1021BF0420")

    def test3(self):
        plain_text = "Attack at dawn"
        key = "Secret"
        self.assertEqual(encrypt(plain_text, key), "45A01F645FC35B383552544B9BF5")


if __name__ == '__main__':
    unittest.main()