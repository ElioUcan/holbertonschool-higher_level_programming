#!/usr/bin/env python3
"""
Serialize and deserialize custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """Class representing a custom object with pickle support."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes and returns an instance from a file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
