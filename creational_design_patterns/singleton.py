class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def __init__(self):
        if not self.__instance:
            print('common instance not created yet.')
        self.val = 0

    def function(self):
        print(self.val)


singleton = Singleton.get_instance()
singleton.function()
singleton.val = 10
singleton.function()


b = Singleton.get_instance()
b.function()


class Singleton:
    class __Singleton:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + ' ' + self.val

    __instance = None

    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance


singleton = Singleton()
singleton.val = 'test'
print(singleton)
singleton_b = Singleton()
print(singleton_b)
singleton_b.val = 'test_b'
print(singleton_b)


def Singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]
    return get_instance


@Singleton
class FirstClass:
    def __init__(self):
        self.val = 0


@Singleton
class SecondClass:
    def __init__(self):
        self.val = 0


first_class = FirstClass()
print(first_class.val)
first_class.val = 100
first_class_b = FirstClass()
print(first_class_b.val)


second_class = SecondClass()
print(second_class.val)
second_class.val = 129
second_class_b = SecondClass()
print(second_class_b.val)


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonType):
    pass


singleton = SingletonClass()
singleton_b = SingletonClass()

print(singleton == singleton_b)


