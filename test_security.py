import unittest

from secure_auth import hash_password, verify_password
from message_integrity import (
    generate_key,
    sign_message,
    verify_message,
)


class TestSecurityProtocols(unittest.TestCase):

    def test_correct_password(self):
        password = "SecurePassword123!"
        salt, stored_hash = hash_password(password)
        self.assertTrue(
            verify_password(password, salt, stored_hash)
        )

    def test_wrong_password(self):
        salt, stored_hash = hash_password("CorrectPassword")
        self.assertFalse(
            verify_password("WrongPassword", salt, stored_hash)
        )

    def test_unique_salts(self):
        salt1, hash1 = hash_password("SamePassword")
        salt2, hash2 = hash_password("SamePassword")
        self.assertNotEqual(salt1, salt2)
        self.assertNotEqual(hash1, hash2)

    def test_message_integrity(self):
        key = generate_key()
        message = "Secure transaction"
        signature = sign_message(message, key)
        self.assertTrue(
            verify_message(message, signature, key)
        )

    def test_tampered_message(self):
        key = generate_key()
        signature = sign_message("Transfer $100", key)
        self.assertFalse(
            verify_message("Transfer $10000", signature, key)
        )

    def test_wrong_key(self):
        key1 = generate_key()
        key2 = generate_key()
        message = "Authenticated message"
        signature = sign_message(message, key1)
        self.assertFalse(
            verify_message(message, signature, key2)
        )


if __name__ == "__main__":
    unittest.main()
