class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health

    def __str__(self):
        return f"{self.name}\n{self.power}\n{self.health}"


# TODO: Create Superhero instances
superhero_one = SuperHero("Batman", "Intelligence", 100)
superhero_two = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(superhero_one)
print(superhero_two)