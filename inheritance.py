# Base class: Animal
class Animal:
    def __init__(self, name, species):
        self.name = name            # Common attribute: name of the animal
        self.species = species      # Common attribute: species of the animal

    def speak(self):
        return f"{self.name} makes a sound."


# Child class 1: Lemur inherits from Animal
class Lemur(Animal):
    def __init__(self, name, facial_color_pattern, grooming_claw):
        super().__init__(name, "Lemur")                     # Initialize base class attributes
        self.facial_color_pattern = facial_color_pattern    # Unique attribute: facial color pattern of the lemur
        self.grooming_claw = grooming_claw                  # Unique attribute: presence of a grooming claw

    def speak(self):
        return f"{self.name} howls."


# Child class 2: Bat inherits from Animal
class Bat(Animal):
    def __init__(self, name, hematophagy, wingspan):
        super().__init__(name, "Bat")    # Initialize base class attributes
        self.hematophagy = hematophagy   # Unique attribute: presence of hematophagy
        self.wingspan = wingspan         # Unique attribute: wingspan in cm

    def speak(self):
        return f"{self.name} squeaks."
