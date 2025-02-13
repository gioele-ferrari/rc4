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

    def test4(self):
        cipher_text = "BBF316E8D940AF0AD3"
        key = "Key"
        self.assertEqual(decrypt(cipher_text, key), "Plaintext")

    def test5(self):
        cipher_text = "1021BF0420"
        key = "Wiki"
        self.assertEqual(decrypt(cipher_text, key), "pedia")

    def test6(self):
        cipher_text = "45A01F645FC35B383552544B9BF5"
        key = "Secret"
        self.assertEqual(decrypt(cipher_text, key), "Attack at dawn")


if __name__ == '__main__':
    unittest.main()