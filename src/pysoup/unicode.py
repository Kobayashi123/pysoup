#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
unicode.py：Converts strings to Unicode and displays them.
"""

__author__ = "Kobayashi Shun"
__version__ = "0.1.0"
__date__ = "2023/11/09 (Created: 2022/11/01)"


def interactive() -> None:
    """
    Interactive mode.
    """
    print("Unicodeに変換する文字列を入力してください")
    print("^d または exit, quit を入力することで終了します")

    while True:
        try:
            input_str = input("> ")
            if input_str in ("exit", "quit"):
                break
        except EOFError:
            print("終了します")
            break

        print_unicode(input_str)

        print_utf8(input_str)


def print_unicode(a_str: str, encode: bool = True) -> None:
    """
    Converts strings to Unicode and displays them.
    """
    if encode:
        unicode_line = encode_unicode(a_str)
        print("Unicode: " + str(unicode_line)[2:-1].replace("\\\\u", " "))
    else:
        unicode_line = decode_unicode(a_str)
        print("String: " + unicode_line)


def encode_unicode(input_str: str) -> bytes:
    """
    Converts strings to Unicode.
    """
    unicode_line = input_str.encode("unicode-escape")
    return unicode_line


def decode_unicode(input_str: str) -> str:
    """
    Converts Unicode to strings.
    """
    str_line = input_str.decode("unicode-escape")
    return str_line


def print_utf8(a_str: str, encode: bool = True) -> None:
    """
    Converts strings to UTF-8 and displays them.
    """
    if encode:
        utf8_line = str(encode_utf8(a_str))
        print("UTF-8: " + utf8_line[2:-1].replace("\\x", "%"))
        print("UTF-8 hex: " + str(utf8_line.replace("\\x", " ")))
    else:
        utf8_line = decode_utf8(a_str)
        print("String: " + utf8_line)


def encode_utf8(input_str: str) -> bytes:
    """
    Converts strings to UTF-8.
    """
    utf8_line = input_str.encode("utf-8")
    return utf8_line


def decode_utf8(input_str: bytes) -> str:
    """
    Converts UTF-8 to strings.
    """
    str_line = input_str.decode("utf-8")
    return str_line


def main():
    """
    Main function of unicode.py when running from command line.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Converts strings to Unicode and displays them.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("-a", "--argument", help="command line argument")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive mode")
    parser.add_argument("-d", "--decode", action="store_true", help="decode unicode")

    args = parser.parse_args()

    print(args)

    if args.argument:
        print_unicode(args.argument)
    elif args.interactive:
        interactive()
    elif args.decode:
        print.unicode(args.argument, False)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
