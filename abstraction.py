from abc import ABC, abstractmethod

# Abstract Base Class: defines the interface and structure for subclasses
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # Common attribute for all animals

    # Abstract method: must be implemented by any subclass
    @abstractmethod
    def make_sound(self):
        pass

    # Regular method: shared behavior that subclasses can use
    def describe(self):
        return f"This is an animal named {self.name}."

# Concrete Child Class: inherits from Animal and implements the abstract method
class Dog(Animal):
    def make_sound(self):
        # Implementation of the abstract method
        return f"{self.name} says Woof!"

# Create an object of the Dog class
my_dog = Dog("Buddy")

# Use the inherited regular method from the parent class
print(my_dog.describe())        # Output: This is an animal named Buddy.

# Use the implemented abstract method from the child class
print(my_dog.make_sound())      # Output: Buddy says Woof!
