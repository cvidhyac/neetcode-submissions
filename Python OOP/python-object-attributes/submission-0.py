class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

    def __str__(self):
        return f"{self.name} ({self.species}) - Hunger: {self.hunger}, Energy: {self.energy}"

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes
print(f"Initial Attributes: {whiskers}")

whiskers.hunger -= 3
whiskers.energy += 2

print(f"Modified Attributes: {whiskers}")