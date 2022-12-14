#!/usr/bin/python3
"""Module 1-number_of_lines.
Counts number of lines in a file.
"""


def write_file(filename="", text=""):
    """Counts lines in filename.

    Args:
        - filename: name of the file

    Returns:
        - number of lines
    """

    count = 0

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
