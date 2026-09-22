#!/usr/bin/env python3

"""
Adds the functionality to serialize
a Python dictionary to a JSON file and deserialize
the JSON file to recreate a Python dictionary

"""

import json


def serialize_and_save_to_file(data, filename):
    """serialize and saves a file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize a file"""

    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
