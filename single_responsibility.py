"""
Animal class violates Single Responsibility Principle
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return f'My name is: {self.name}'

    def save(self, animal):
        pass


"""
How it should be? See:
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'My name is {self.name}'


class AnimalDB:
    def get_animal(self, primary_key) -> Animal:
        pass

    def save(self, animal: Animal):
        pass


"""
Update. Use facade
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return f'My name is: {self.name}'

    def get(self, primary_key):
        return self.db.get_animal(primary_key)

    def save(self):
        self.db.save(animal=self)


animal = Animal('Lion')
animal.save()
