"""inheritance is called oop's pillar
    it allows a class to inherit attributes and methods from another class
    it promotes code reusability and establishes a hierarchical relationship between classes
    """

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# Example usage
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows

# Demonstrating multi-level inheritance
class Puppy(Dog):
    def speak(self):
        return "Puppy yaps"
puppy = Puppy()
print(puppy.speak())  # Output: Puppy yaps
