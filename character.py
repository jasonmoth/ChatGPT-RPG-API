from being import Being

class Character(Being):
    def __init__(self, name, character_class, level):
        super().__init__(name, character_class, level)
        # Add any character-specific attributes here




# Was generalized to BEING
#
# class Character:
#     def __init__(self, name, character_class, level):
#         self.name = name
#         self.character_class = character_class
#         self.level = level
#         self.skills = []
#         self.spells = []
#         self.equipped_items = []
#         self.inventory = []

#         self.head_slot = None
#         self.body_slot = None
#         self.footware_slot = None

#         self.left_hand_accessory_slot = None
#         self.right_hand_accessory_slot = None
#         self.body_accessory_slot = None
#         self.amulet_slot = None

#         self.right_hand_weapon_slot = None
#         self.left_hand_weapon_slot = None


#     def add_skill(self, skill):
#         self.skills.append(skill)

#     def add_spell(self, spell):
#         self.spells.append(spell)

#     def equip_item(self, item):
#         self.equipped_items.append(item)