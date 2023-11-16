#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
check_link.py：Check the links in the HTML file.
"""

__author__ = "Kobayashi Shun"
__version__ = "0.1.0"
__date__ = "2023/11/16 (Created: 2023/11/7)"

import argparse
import sys

import requests
from bs4 import BeautifulSoup


def check_link(html_file=None, url=None):
    """
    Check the links in the HTML file.
    """
    html_source = None

    if html_file:
        html_source = get_source_from_html(html_file)
    elif url:
        html_source = get_source_from_link(url)
    else:
        print("Error: No input.")
        return 1

    links = get_link_from_html(html_source)
    for link in links:
        print(link)


def get_source_from_html(html_file: str) -> str:
    """
    Get the text from the HTML file.
    """
    try:
        with open(html_file, "r", encoding="utf-8") as a_file:
            html = a_file.read()
    except FileNotFoundError as err:
        print(f"Error: {err}")
        return 1

    return html


def get_source_from_link(link: str) -> str:
    """
    Get the text from the link.
    """
    try:
        response = requests.get(link)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return 1


def get_link_from_html(html_source: str) -> list:
    """
    Get the links from the HTML source.
    """

    beautiful_soup = BeautifulSoup(html_source, "html.parser")

    href_list = list()
    for a in beautiful_soup.find_all("a"):
        a_href = a.get("href")
        if a_href is None:
            continue
        if a_href.startswith("http"):
            href_list.append(a_href)

    href_list = list(set(href_list))

    img_src_list = list()
    for img in beautiful_soup.find_all("img"):
        img_src = img.get("src")
        if img_src.startswith("http"):
            img_src_list.append(img_src)

    img_src_list = list(set(img_src_list))

    return href_list + img_src_list


def main():
    """
    Main function of check_link.py when running from command line.
    """

    parser = argparse.ArgumentParser(description="Check the links in the HTML file.")
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("-f", "--file", action="store", type=str, help="HTML file to check the links.")
    parser.add_argument("-u", "--url", action="store", type=str, help="URL to check the HTML file.")
    args = parser.parse_args()

    check_link(html_file=args.file, url=args.url)


if __name__ == "__main__":
    sys.exit(main())
