import hashlib
import hmac
import secrets


def generate_key():
    return secrets.token_bytes(32)


def sign_message(message, key):
    return hmac.new(
        key,
        message.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def verify_message(message, signature, key):
    expected = sign_message(message, key)
    return hmac.compare_digest(expected, signature)


if __name__ == "__main__":
    key = generate_key()
    original_message = "Transfer $100"
    signature = sign_message(original_message, key)

    print("Cryptographic Message Integrity Demo")
    print("Original message:", original_message)
    print("Signature:", signature)

    print(
        "Original verified:",
        verify_message(original_message, signature, key)
    )

    tampered_message = "Transfer $10000"

    print(
        "Tampered verified:",
        verify_message(tampered_message, signature, key)
    )
