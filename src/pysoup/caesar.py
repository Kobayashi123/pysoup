#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
caesar.py: Encrypt the input text with the Caesar cipher.
"""

__author__ = "Kobayashi Shun"
__version__ = "0.1.0"
__date__ = "2023/11/11 (Created: 2023/05/28)"


def encrypt(plain: str, key: int) -> str:
    """
    Encrypt plain text with the Caesar cipher, shifting the letters by the number given by key.
    """
    cipher = ""
    for char in plain:
        if char.isalpha():
            # Encrypt uppercase characters in plain text
            if char.isupper():
                cipher += chr((ord(char) - 65 + key) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                cipher += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            cipher += char
    print("Cipher:  " + cipher)


def decrypt(cipher: str, key: int) -> str:
    """
    Decrypts cipher text with the Caesar cipher, shifting the letters by the number given by key.
    """
    plain = ""
    for char in cipher:
        if char.isalpha():
            # Encrypt uppercase characters in plain text
            if char.isupper():
                plain += chr((ord(char) - 65 - key) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                plain += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            plain += char
    print("Plain:  " + plain)


def main():
    """
    Main function of caesar.py when running from command line.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt the input text with the Caesar cipher.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("argument", default=True, type=str, help="command line argument")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive mode")
    parser.add_argument("-e", "--encrypt", default=True, action="store_true", help="encrypt mode")
    parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt mode")
    parser.add_argument("-k", "--key", default=1, type=int, help="cipher key")

    args = parser.parse_args()

    if args.decrypt:
        decrypt(args.argument, args.key)
    elif args.encrypt:
        encrypt(args.argument, args.key)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
