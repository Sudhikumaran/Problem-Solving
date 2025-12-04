"""Types of methods in Python classes.
1. Instance Methods: The most common type of method, which operates on an instance of the class. It takes 'self' as the first parameter.
2. Class Methods: These methods operate on the class itself rather than on instances. They take 'cls' as the first parameter and are decorated with @classmethod.
3. Static Methods: These methods do not operate on an instance or the class. They do not take 'self' or 'cls' as the first parameter and are decorated with @staticmethod."""

class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Instance Method
    def instance_method(self):
        return f"Instance Method called. Instance Variable: {self.instance_variable}"

    # Class Method
    @classmethod
    def class_method(cls):
        return f"Class Method called. Class Variable: {cls.class_variable}"

    # Static Method
    @staticmethod
    def static_method():
        return "Static Method called. No access to instance or class variables."
# Creating an instance of MyClass
obj = MyClass("I am an instance variable")
# Calling Instance Method
print(obj.instance_method())
# Calling Class Method
print(MyClass.class_method())
# Calling Static Method
print(MyClass.static_method())
