# Security Report — Secure File Encryption Tool

## 1. Project Objective

The objective of this project is to build a local file encryption tool that protects files from unauthorized access using password-based encryption.

## 2. Assets Protected

The main asset protected by this tool is the content of local files selected by the user.

Examples:
- Text files
- PDF files
- Notes
- Small local documents

## 3. Threat Model

### Threats considered

- Unauthorized access to sensitive files
- Reading files without the correct password
- Modification of encrypted files
- Wrong password attempts

### Threats not covered

- Malware already installed on the computer
- Keyloggers
- Weak or reused passwords
- Physical compromise of the machine
- Social engineering attacks

## 4. Cryptographic Design

The tool uses AES-GCM for authenticated encryption.

AES-GCM provides:
- Confidentiality: the file content is encrypted
- Integrity: modification of the encrypted data can be detected
- Authentication: decryption fails if the tag is invalid

The encryption key is derived from the user password using PBKDF2.

For every encryption operation, the tool generates:
- A random salt
- A random nonce

## 5. Security Controls Implemented

- Password input is hidden in the terminal
- Password is not stored
- Salt is randomly generated
- Nonce is randomly generated
- Decryption fails if the password is wrong
- Decryption fails if the encrypted file is corrupted
- Input and output file paths are validated

## 6. Error Handling

The tool handles common errors such as:
- Missing input file
- Invalid encrypted file format
- Wrong password
- Corrupted encrypted file
- Same input and output file path

## 7. Limitations

This tool is designed for educational and portfolio purposes.

It has not been independently audited and should not be used as a replacement for production-grade encryption tools.

## 8. Recommendations

Users should:
- Use long and unique passwords
- Keep backups of important files
- Avoid decrypting files on untrusted machines
- Avoid sharing passwords
- Store encrypted files safely