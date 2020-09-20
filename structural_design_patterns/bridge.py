class Drink:
    def get_volume(self):
        pass

    def is_addictive(self):
        pass

    def get_number_of_sugar_lumps(self):
        pass

    def get_taste(self):
        pass


class Coffee(Drink):
    def get_volume(self):
        return 150

    def is_addictive(self):
        return True

    def get_number_of_sugar_lumps(self):
        return 0

    def get_taste(self):
        return 'bitter'


class Tea(Drink):
    def get_volume(self):
        return 250

    def is_addictive(self):
        return False

    def get_number_of_sugar_lumps(self):
        return 2

    def get_taste(self):
        return 'sweet'


class DrinkPurchase:
    def buy(self, cost):
        pass


class CoffeePurchase(DrinkPurchase):
    def buy(self, cost):
        print(f'Buying coffee, cost: {cost}')
        return Coffee()


class TeaPurchase(DrinkPurchase):
    def buy(self, cost):
        print(f'Buying tea, cost {cost}')
        return Tea()


tea_cost = 12
print(TeaPurchase().buy(tea_cost))
print(CoffeePurchase().buy(14))
