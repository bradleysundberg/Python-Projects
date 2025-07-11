# Parent class: Animal
class Animal:
    def __init__(self, name, species):
        self.name = name            # Common attribute: name of the animal
        self.species = species      # Common attribute: species of the animal

    def speak(self):
        # Method to be overridden by child classes
        return f"{self.name} makes a sound."


# Child class 1: Lemur inherits from Animal
class Lemur(Animal):
    def __init__(self, name, facial_color_pattern, grooming_claw):
        # Initialize attributes from the parent class
        super().__init__(name, species="Lemur")
        self.facial_color_pattern = facial_color_pattern  # Specific to lemur
        self.grooming_claw = grooming_claw                # Specific to lemur (True/False)

    def speak(self):
        # Overridden method to demonstrate polymorphism
        return f"{self.name} the lemur chitters and makes a clicking sound."


# Child class 2: Bat inherits from Animal
class Bat(Animal):
    def __init__(self, name, wing_span_cm, echolocation_ability):
        # Initialize attributes from the parent class
        super().__init__(name, species="Bat")
        self.wing_span_cm = wing_span_cm                 # Specific to bat
        self.echolocation_ability = echolocation_ability # Specific to bat (True/False)

    def speak(self):
        # Overridden method to demonstrate polymorphism
        return f"{self.name} the bat emits high-pitched echolocation clicks."


# --- Example usage demonstrating polymorphism ---
animals = [
    Lemur("Zoboo", facial_color_pattern="black-and-white", grooming_claw=True),
    Bat("Nocturne", wing_span_cm=35, echolocation_ability=True)
]

# Loop through each animal and call the speak() method
for animal in animals:
    print(animal.speak())  # Demonstrates polymorphism
