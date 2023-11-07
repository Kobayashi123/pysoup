#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
map_it.py：住所からGoogleマップを開きます
"""

__author__ = "kobayashi shun"
__version__ = "1.0.0"
__date__ = "2023/11/05 (Created: 2023/11/05)"

import sys
import urllib.parse
import webbrowser
from typing import List, Optional


def main(args: Optional[List[str]] = None) -> int:
    """
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    if args is None:
        args = sys.argv[1:]

    if len(args) < 1:
        print("住所を指定してください。")
        return 1
    else:
        address = "".join(args)

    webbrowser.open("https://www.google.com/maps/place/" + urllib.parse.quote(address), new=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="display google map from input location.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("location", metavar="location", type=str, help="input location")
    parser.add_argument("-c", "--clipboard", action="store_true", help="use clipboard text")
    args = parser.parse_args()

    sys.exit(main(args.location))
