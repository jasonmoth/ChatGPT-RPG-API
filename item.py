class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

class Weapon(Item):
    def __init__(self, name, value, weight, damage):
        super().__init__(name, value, weight)
        self.damage = damage

class Armor(Item):
    def __init__(self, name, value, weight, defense):
        super().__init__(name, value, weight)
        self.defense = defense

class Shield(Item):
    def __init__(self, name, value, weight):
        super().__init__(name, value, weight)

class Potion(Item):
    def __init__(self, name, value, weight, effect, duration, duration_units='TURNS'):
        super().__init__(name, value, weight)
        self.effect = effect
        self.duration = duration
        self.duration_units = duration_units