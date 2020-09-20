class Cook:
    """
    Director - managing object creation
    """
    def __init__(self):
        self._builder = None

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()


class PizzaBuilder:
    """
    Builder - abstract interface
    """

    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self):
        pass

    def add_extras(self):
        pass

    def bake(self):
        pass


class MargaritaBuilder(PizzaBuilder):
    """
    ConcreteBuilder - creates concrete object
    """
    def prepare_dough(self):
        pass

    def add_extras(self):
        pass

    def bake(self):
        pass


class PepperoniBuilder(PizzaBuilder):
    """
    ConcreteBuilder - creates concrete object
    """

    def prepare_dough(self):
        pass

    def add_extras(self):
        pass

    def bake(self):
        pass


class Pizza:
    """
    Generated complex object
    """


cook = Cook()
baking = PepperoniBuilder()
cook.prepare(baking)
pizza = baking.pizza
print(pizza)
