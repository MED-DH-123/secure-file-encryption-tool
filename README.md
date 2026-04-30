# Secure File Encryption Tool

A Python command-line tool for encrypting and decrypting local files using AES-GCM and PBKDF2.

## Overview

This project demonstrates secure file encryption, password-based key derivation, command-line interface design, and basic secure coding practices.

The tool allows a user to:
- Encrypt a file using a password
- Decrypt the encrypted file using the correct password
- Detect wrong passwords or corrupted encrypted files
- Use a simple CLI interface

## Features

- File encryption
- File decryption
- AES-GCM authenticated encryption
- PBKDF2 key derivation
- Random salt generation
- Random nonce generation
- Hidden password input
- Error handling
- Security report included

## Technologies Used

- Python
- PyCryptodome
- AES-GCM
- PBKDF2
- Git / GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/MED-DH-123/secure-file-encryption-tool.git
cd secure-file-encryption-tool
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Create a test file:

```bash
echo "This is a secret file for encryption testing" > secret.txt
```

Encrypt the file:

```bash
python encryptor.py encrypt -i secret.txt -o secret.enc
```

Decrypt the file:

```bash
python encryptor.py decrypt -i secret.enc -o decrypted.txt
```

Verify the decrypted content:

```bash
cat decrypted.txt
```

## Error Handling Examples

Wrong password or corrupted file:

```text
[ERROR] Decryption failed. Wrong password or corrupted file.
```

Missing input file:

```text
[ERROR] Input file not found.
```

## Security Design

This project uses:

- AES-GCM for authenticated encryption
- PBKDF2 for password-based key derivation
- Random salt for each encryption operation
- Random nonce for each encryption operation
- Hidden password input using getpass

The password is not stored by the program.

## Limitations

This is an educational cybersecurity project. It is not a replacement for professionally audited encryption software.

The tool does not protect against:

- Malware already running on the machine
- Keyloggers
- Weak passwords
- Users sharing passwords
- Loss of the encryption password

## Project Status

Completed as a cybersecurity portfolio project.

## Author

MED-DH-123