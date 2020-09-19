"""
Animal example violating Liskov Substitution Principle
"""

DEFAULT_LION_LEG_COUNT = 4
DEFAULT_ELEPHANT_LEG_COUNT = 4
DEFAULT_PYTHON_LEG_COUNT = 0


class Animal:
    pass


class Lion(Animal):
    pass


class Elephant(Animal):
    pass


class Python(Animal):
    pass


def animal_leg_count(animals):
    for animal in animals:
        if isinstance(animal, Lion):
            print(DEFAULT_LION_LEG_COUNT)
        elif isinstance(animal, Elephant):
            print(DEFAULT_ELEPHANT_LEG_COUNT)
        elif isinstance(animal, Python):
            print(DEFAULT_PYTHON_LEG_COUNT)


animals = [
    Lion(),
    Elephant(),
    Python()
]

animal_leg_count(animals)


"""
Animal example according to Liskov Substitution Principle
"""


class Animal:
    def get_legs_count(self):
        pass


class Lion(Animal):
    def get_legs_count(self):
        return DEFAULT_LION_LEG_COUNT


class Elephant(Animal):
    def get_legs_count(self):
        return DEFAULT_ELEPHANT_LEG_COUNT


class Python(Animal):
    def get_legs_count(self):
        return DEFAULT_PYTHON_LEG_COUNT


def animal_leg_count(animals):
    for animal in animals:
        print(animal.get_legs_count())


animals = [
    Lion(),
    Elephant(),
    Python()
]

animal_leg_count(animals)
