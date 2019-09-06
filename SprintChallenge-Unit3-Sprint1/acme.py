from random import randint


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal_value = self.price / self.weight

        if steal_value < 0.5:
            return 'Not so stealable...'
        elif steal_value >= 0.5 and steal_value < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        explode_value = self.flammability * self.weight

        if explode_value < 10:
            return '...fizzle'
        elif explode_value >= 10 and explode_value < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, weight=10):
        super().__init__(name, weight=weight)

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
