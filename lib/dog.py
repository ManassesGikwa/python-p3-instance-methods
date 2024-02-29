#!/usr/bin/env python3

# In lib/dog.py

class Dog:
    def __init__(self, name, age):
        self.name = name


class Dog:
    def __init__(self, name="DefaultName", age=0):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
