#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
scraping.py：Scraping to obtain and display built-in functions.
"""

__author__ = "Kobayashi Shun"
__version__ = "0.1.0"
__date__ = "2023/11/03 (Created: 2023/09/06)"

import os

import requests
from bs4 import BeautifulSoup


def main() -> int:
    """
    Main function of scraping.py when running from command line.
    """

    table_python3 = table_of_builtin_function_and_hyper_reference("https://docs.python.org/3.7/library/functions.html")
    table_python2 = table_of_builtin_function_and_hyper_reference("http://docs.python.jp/2.7/library/functions.html")
    if (table_python2 is None) or (table_python3 is None):
        return 1

    table = dict()
    for key in table_python3:
        table[key] = [3, 0]  # exists in Python 3
    for key in table_python2:
        if key in table:
            table[key] = [3, 2]  # also exists in Python 2
        else:
            table[key] = [0, 2]  # only exists in Python 2

    directory = os.path.dirname(__file__)

    if not os.path.isdir(os.path.join(directory, "output")):
        os.mkdir(os.path.join(directory, "output"))

    a_file = os.path.join(directory, "output", "built_in_function.html")

    with open(a_file, "w", encoding="utf-8") as a_file:
        a_file.write(head_part())
        a_file.write('<table class="content" summary="table">\n')
        a_file.write("  <tbody>\n")
        a_file.write("    <tr>\n")
        a_file.write('      <td class="center-border">Python 3 組み込み関数</td>\n')
        a_file.write('      <td class="center-border">Python 2 組み込み関数</td>\n')
        a_file.write("    </tr>\n")

        td_string0 = '      <td class="center-border">---</td>\n'

        for key, value in sorted(table.items()):
            builtin_function = key
            a_file.write("    <tr>\n")
            if (value[0] == 0) and (value[1] == 0):  # does not exist in Python 3 and 2
                pass
            if (value[0] == 3) and (value[1] == 0):  # only exists in Python 3
                hyper_reference = table_python3[builtin_function]
                a_file.write(
                    f'      <td class="center-border"><a href="{hyper_reference}" title="Python3">{builtin_function}</a></td>\n'
                )
                a_file.write(td_string0)
            if (value[0] == 0) and (value[1] == 2):  # only exists in Python 2
                a_file.write(td_string0)
                hyper_reference = table_python2[builtin_function]
                a_file.write(
                    f'      <td class="center-border"><a href="{hyper_reference}" title="Python2">{builtin_function}</a></td>\n'
                )
            if (value[0] == 3) and (value[1] == 2):  # exists in Python 3 and 2
                hyper_reference = table_python3[builtin_function]
                a_file.write(
                    f'      <td class="center-border"><a href="{hyper_reference}" title="Python3">{builtin_function}</a></td>\n'
                )
                hyper_reference = table_python2[builtin_function]
                a_file.write(
                    f'      <td class="center-border"><a href="{hyper_reference}" title="Python2">{builtin_function}</a></td>\n'
                )
            a_file.write("    </tr>\n")

        a_file.write("  </tbody>\n")
        a_file.write("</table>\n")
        a_file.write(foot_part())

    return 0


def head_part() -> str:
    """
    Responds to the header section.
    """

    return """<!DOCTYPE html>

<html lang="ja">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="Content-Style-Type" content="text/css">
        <meta http-equiv="Content-Script-Type" content="text/javascript">
        <meta name="keywords" content="Python,Pythonist,Functional,BuildInFunction">
        <meta name="description" content="組み込み関数-Python">
        <meta name="author" content="Kobayashi Shun">
        <link rel="index" href="index-j.html">
        <style type="text/css">
        <!--
        body {
            background-color : #ffffff;
            margin : 20px;
            padding : 10px;
            font-family : serif;
            font-size : 12pt;
        }
        div {
        display: flex;
        }
        table.content {
            border-style : solid;
            border-width : 0px;
            border-color : #ffffff;
        }
        .center-border {
            text-align : center;
            vertical-align : middle;
            empty-cells : show;
            border-style : solid;
            border-width : 1px;
            border-color : #ffc080;
            width : 350px;
            height : 22px;
        }
        -->
        </style>
        <title>組み込み関数-Python</title>
    </head>

    <body>
        <h1>Pythonの組み込み関数</h1>

            Python 2系 の公式ドキュメントはこちら : <a href="https://docs.python.org/ja/2.7/library/functions.html">
                https://docs.python.org/ja/2.7/library/functions.html</a><br>
            Python 3系 の公式ドキュメントはこちら : <a href="https://docs.python.org/ja/3.11/library/functions.html">
                https://docs.python.org/ja/3.11/library/functions.html</a>

        <div>
"""


def foot_part() -> str:
    """
    Responds to the footer section.
    """

    return """        </div>
    </body>
</html>
"""


def table_of_builtin_function_and_hyper_reference(the_url_string: str) -> tuple:
    """
    Web scraping of Python built-in function web pages,
    creating a dictionary of built-in function names and hyperlinks to respond.
    """

    response = requests.get(the_url_string)
    if response.status_code != 200:
        return None

    response.encoding = response.apparent_encoding
    html_source = response.text

    beautiful_soup = BeautifulSoup(html_source, "html.parser")

    table_tag = beautiful_soup.find(name="table", attrs={"class": "docutils"})
    if table_tag is None:
        return None

    table = dict()
    for td_tag in table_tag.find_all(name="td"):
        a_tag = td_tag.find(name="a", attrs={"class": "reference internal"})
        if a_tag is not None:
            builtin_function = td_tag.string.strip()
            hyper_reference = the_url_string + a_tag["href"]
            table[builtin_function] = hyper_reference

    return table


if __name__ == "__main__":
    import sys

    sys.exit(main())
