#!/usr/bin/env python3

"""

Module to convert forom csv to Json

"""

import csv
import json

def convert_csv_to_json(filename):
    """converts csv to json"""
    try: 
        with open(filename, "r", encoding="utf-8") as f:
            read = csv.DictReader(f)
            data = list(read)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return True

    except Exception as e:
        return False

