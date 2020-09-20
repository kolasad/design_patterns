import pickle


class NotSoSimpleClass:
    def __init__(self, name='', count=0):
        self.name = name
        self.count = count

    def get_state(self):
        return pickle.dumps(self.__dict__)

    def restore_state(self, memento):
        self.__dict__.clear()
        self.__dict__.update(pickle.loads(memento))


sc1 = NotSoSimpleClass('test', 10)
memento = sc1.get_state()
sc2 = NotSoSimpleClass()
sc2.restore_state(memento)
print(sc1.name, sc1.count)
print(sc2.name, sc2.count)
