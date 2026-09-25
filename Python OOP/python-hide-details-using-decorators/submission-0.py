class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.__name = name
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods
    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, val) -> None:
        self.__name = val
    
    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, val):
        if val in range(101):
            self.__health = val
        if val < 0:
            print("You can't set the health to less than 0")
        if val > 100:
            print("You can't set the health to more than 100")

    @property
    def power_level(self):
        return self.__power_level

    @power_level.setter
    def power_level(self, val):
        if val > 10:
            print("You can't set the power level to more than 10")
        if val < 1:
            print("You can't set the power level to less than 1")
        if val in range(11):
            self.__power_level = val

# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power_level) # this should print 9
super_hero.power_level = 100 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1

super_hero.power_level = 9
# TODO: print the hero's attributes 
print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")