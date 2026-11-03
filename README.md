# Secure Authentication & Cryptographic Protocols

## Overview
A Python security engineering project demonstrating secure password authentication, cryptographic message integrity, and automated security testing.

This project explores foundational security software engineering concepts relevant to authentication systems and secure communication protocols.

## Technologies
- Python 3
- PBKDF2-HMAC-SHA256
- HMAC-SHA256
- Python unittest
- GitHub Actions
- GitHub

## Security Features

### Secure Password Authentication
- PBKDF2-HMAC-SHA256 password hashing
- 600,000 PBKDF2 iterations
- Cryptographically random 16-byte salts
- Constant-time hash comparison
- Correct and incorrect password verification

### Cryptographic Message Integrity
- HMAC-SHA256 message authentication
- Cryptographically random 32-byte keys
- Detection of message tampering
- Rejection of incorrect authentication keys
- Constant-time signature comparison

## Architecture

Password Authentication:
User Password -> Random Salt -> PBKDF2-HMAC-SHA256 -> Stored Salt and Hash -> Verification

Message Authentication:
Message + Secret Key -> HMAC-SHA256 -> Authentication Tag -> Integrity Verification

## Automated Security Testing

The project uses Python unittest and GitHub Actions for continuous integration.

Verified test results:
- Correct password authentication: PASS
- Incorrect password rejection: PASS
- Unique password salts: PASS
- Message integrity verification: PASS
- Tampered message detection: PASS
- Incorrect cryptographic key rejection: PASS

**Result: 6 tests passed (GitHub Actions).**

## Running the Tests

```bash
python -m unittest discover -v
```

## Project Files
- `secure_auth.py` — Password hashing and verification
- `message_integrity.py` — HMAC message authentication
- `test_security.py` — Automated security tests
- `.github/workflows/security-tests.yml` — CI workflow

## Security Considerations
- Passwords are not stored in plaintext by the demonstration.
- HMAC provides message integrity and authentication, not encryption.
- Cryptographic keys must be protected in production systems.
- This is an educational implementation, not a production-ready authentication service.
- Production systems also require secure secret storage, rate limiting, authorization, monitoring, and threat modeling.

## Skills Demonstrated
Python programming, secure authentication, cryptographic primitives, security testing, continuous integration, and secure software development.

## Author
David Jeffries
