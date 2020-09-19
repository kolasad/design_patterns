"""
Animal class violates Open-Closed Principle
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'My name is: {self.name}'


def animal_sound(animals):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar!!!')
        elif animal.name == 'Elephant':
            print('Pffff!!!')


animals = [
    Animal('Lion'),
    Animal('Elephant')
]

animal_sound(animals)

# If we want to add new animal, then we should modify the method, not extend it.
# That's why it violates Open-Closed Principle.

animals = [
    Animal('Lion'),
    Animal('Elephant'),
    Animal('Python')
]


def animal_sound(animals):
    for animal in animals:
        if animal.name == 'Lion':
            print('Roar!!!')
        elif animal.name == 'Elephant':
            print('Pffff!!!')
        elif animal.name == 'Python':
            print('Sssss!!!')


animal_sound(animals)


"""
How to make it according to Open-Closed Principle?
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'My name is: {self.name}'

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'Roar!!!'


class Elephant(Animal):
    def make_sound(self):
        return 'Pffff!!!'


# If we want to add new animal, then we can extend from Animal class.
# That's why it's correct according to Open-Closed Principle.


class Python(Animal):
    def make_sound(self):
        return 'Sssss!!!'


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [
    Lion('Lion'),
    Elephant('Elephant'),
    Python('Super Python')
]

animal_sound(animals)


"""
One more case. Does support Open-Closed Principle
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


"""
If I would add even higher discount I can extend it like this:
"""


class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2


customer, price = 'Jan', 100

assert Discount(customer, price).get_discount() == 20.0
assert VIPDiscount(customer, price).get_discount() == 40.0
assert SuperVIPDiscount(customer, price).get_discount() == 80.0
