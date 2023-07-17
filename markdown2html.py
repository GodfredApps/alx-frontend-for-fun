#!/usr/bin/python3

"""
markdown2html.py

Converts a Markdown file to HTML.

Usage: ./markdown2html.py <markdown_file> <output_file>
"""

import sys
import os
import markdown


def convert_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML.

    Args:
        markdown_file (str): The path to the Markdown file.
        output_file (str): The path to the output HTML file.
    """
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()
        html_text = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_to_html(markdown_file, output_file)
    sys.exit(0)
