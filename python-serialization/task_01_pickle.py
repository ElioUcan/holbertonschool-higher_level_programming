#!/usr/bin/env python3

"""
Serialize class

"""

import pickle


class CustomObject:
    """Class of a custom object"""

    def __init__(self, name, age, is_student):

        self.name = name
        self.age = age
        self.isStudent = is_student

    def display(self):

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.isStudent}")

    def serialize(self, filename):
        """Serializes in a binary file."""
        with open(filename, "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a binary file."""
        with open(filename, "rb") as f:
            obj = pickle.load(f)
        if not isinstance(obj, cls):
            return None

        return obj
