#!/usr/bin/env python3

"""
Serialize class

"""

import pickle
from abc import classmethod


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.isStudent = is_student

    def display(self):

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.isStudent}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(f, protocol=pickle.HIGHEST_PROTOCOL)
        with open(filename, "rb") as f:
            load = pickle.load(f)
        return load

    @classmethod
    def deserialize(cls, filename):
        serialize = pickle.dumps(filename)
        restored = pickle.loads(serialize)
        return restored
