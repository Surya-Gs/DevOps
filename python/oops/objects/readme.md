Objects in python

Objects are variables that contain data and functions that can be used to manipulate the data. The object's data can vary in type (string, integer, etc.) depending on how it’s been defined. An object is like a mini-program inside python, with its own set of rules and behaviors.

In short 
An object is like a mini-program inside python, with its own set of rules and behaviors.



Example:
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Alex', 24)
print(person1.name)
print(person1.age)


here class is a keyword to define a object
The __init__ is a python function that runs when the python object is first created. This function holds all of the data and instructions for the python object.
This python object has two variables (name and age) which can be manipulated by the python code.


The self keyword is just python’s way of letting us know what object we are working with.

