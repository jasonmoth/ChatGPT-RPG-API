class Character:
    def __init__(self, name, character_class, level):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.skills = []
        self.spells = []
        self.equipped_items = []
        self.inventory = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_spell(self, spell):
        self.spells.append(spell)

    def equip_item(self, item):
        self.equipped_items.append(item)
