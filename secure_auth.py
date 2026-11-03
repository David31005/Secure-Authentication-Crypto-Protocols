import hashlib
import hmac
import secrets

ITERATIONS = 600_000


def hash_password(password):
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )
    return salt.hex(), password_hash.hex()


def verify_password(password, salt_hex, stored_hash_hex):
    salt = bytes.fromhex(salt_hex)
    stored_hash = bytes.fromhex(stored_hash_hex)

    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )

    return hmac.compare_digest(new_hash, stored_hash)


if __name__ == "__main__":
    password = "DemoPassword123!"
    salt, stored_hash = hash_password(password)

    print("Secure Authentication Demo")
    print("Password hash:", stored_hash)
    print("Correct password:", verify_password(password, salt, stored_hash))
    print("Wrong password:", verify_password("WrongPassword", salt, stored_hash))
