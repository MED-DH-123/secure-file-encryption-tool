import argparse
import getpass
import os
import sys
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

MAGIC = b"SFE1"
SALT_SIZE = 16
NONCE_SIZE = 16
TAG_SIZE = 16
KEY_SIZE = 32
PBKDF2_ITERATIONS = 200_000


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(
        password,
        salt,
        dkLen=KEY_SIZE,
        count=PBKDF2_ITERATIONS,
        hmac_hash_module=SHA256
    )


def validate_paths(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        raise FileNotFoundError("Input file not found.")

    if os.path.abspath(input_path) == os.path.abspath(output_path):
        raise ValueError("Input and output file cannot be the same.")


def encrypt_file(input_path: str, output_path: str, password: str):
    validate_paths(input_path, output_path)

    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(output_path, "wb") as f:
        f.write(MAGIC)
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f"[OK] File encrypted successfully: {output_path}")


def decrypt_file(input_path: str, output_path: str, password: str):
    validate_paths(input_path, output_path)

    with open(input_path, "rb") as f:
        magic = f.read(4)

        if magic != MAGIC:
            raise ValueError("Invalid encrypted file format.")

        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        tag = f.read(TAG_SIZE)
        ciphertext = f.read()

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    except ValueError:
        raise ValueError("Decryption failed. Wrong password or corrupted file.")

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"[OK] File decrypted successfully: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Secure File Encryption Tool using AES-GCM"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    encrypt_parser.add_argument("-i", "--input", required=True, help="Input file")
    encrypt_parser.add_argument("-o", "--output", required=True, help="Output encrypted file")

    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    decrypt_parser.add_argument("-i", "--input", required=True, help="Input encrypted file")
    decrypt_parser.add_argument("-o", "--output", required=True, help="Output decrypted file")

    args = parser.parse_args()

    password = getpass.getpass("Enter password: ")

    if len(password) < 8:
        print("[ERROR] Password must be at least 8 characters.", file=sys.stderr)
        sys.exit(1)

    try:
        if args.command == "encrypt":
            encrypt_file(args.input, args.output, password)
        elif args.command == "decrypt":
            decrypt_file(args.input, args.output, password)

    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()