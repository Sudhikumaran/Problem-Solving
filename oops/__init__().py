"__init__() method in Python is a special method that is automatically called when a new instance of a class is created. It is commonly used to initialize the attributes of the class. Here is an example of how to use the __init__() method in a class definition:"

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self, another):
        if self.age == another.age:
            return True
        else:
            return False
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
human1 = Human("Sudhi", 20)
human2 = Human("Mahendra", 21)

print(human1.compare(human2))
human1.display()
human2.display()
