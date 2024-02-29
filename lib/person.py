#!/usr/bin/env python3

# In lib/person.py

# In lib/person.py

class Person:
    def __init__(self, name="DefaultName", age=0):
        self.name = name
        self.age = age

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
