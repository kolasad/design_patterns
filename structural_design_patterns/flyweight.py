import random


class Engine:
    instances = 0

    def __init__(self, identifier, volume, engine_type):
        Engine.instances += 1
        self._identifier = identifier
        self._volume = volume
        self._engine_type = engine_type


class Car:
    def __init__(self, producer, vin, model_name, engine):
        self._producer = producer
        self._vin = vin
        self._model_name = model_name
        self._engine = engine


class CarFactory:
    engines = (
        Engine('gt', 2.0, 'GASOLINE'),
        Engine('e', 0.0, 'ELECTRIC'),
        Engine('normal', 1.0, 'DIESEL'),
    )

    @staticmethod
    def create_subaru(vin):
        return Car('Subaru', vin, 'Impreza', CarFactory.engines[0])

    @staticmethod
    def create_polo(vin):
        return Car('VW', vin, 'POLO', CarFactory.engines[2])

    @staticmethod
    def create_tesla(vin):
        return Car('Tesla', vin, '3', CarFactory.engines[1])


produced_cars = []
for i in range(1000):
    engine_type = random.randint(0, 2)
    if engine_type == 0:
        produced_cars.append(CarFactory.create_subaru(random.randint(0, 100000000000)))
    elif engine_type == 1:
        produced_cars.append(CarFactory.create_subaru(random.randint(0, 100000000000)))
    elif engine_type == 2:
        produced_cars.append(CarFactory.create_subaru(random.randint(0, 100000000000)))


print(produced_cars)
