"""getters & setters
there are two ways to access attributes in a class:
1. directly
2. using getter and setter methods
getters are methods that return the value of an attribute
setters are methods that set the value of an attribute
using getters and setters allows for validation and encapsulation"""

class Person:
    def __init__(self, name, age):
        self._name = name  # private attribute
        self._age = age    # private attribute

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age with validation
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

person = Person("Alice", 30)
print(f"Name: {person.get_name()}, Age: {person.get_age()}")
person.set_name("Bob")
person.set_age(25)
print(f"Updated Name: {person.get_name()}, Updated Age: {person.get_age()}")
person.set_age(-5)  # This will trigger the validation message

