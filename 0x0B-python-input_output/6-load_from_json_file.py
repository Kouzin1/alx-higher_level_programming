#!/usr/bin/python3
""" Module that creates an Object fromo a JSON file
"""
import json


def load_from_json_file(filename):
    """ FUnction that creates an Object from a JSON file

    Args:
        filename: textfile name

    Raises:
        Exception: When the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
