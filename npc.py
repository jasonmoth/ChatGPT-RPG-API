from being import Being

class NPC(Being):
    def __init__(self, name, character_class, level, alignment, goals, faction, disposition):
        super().__init__(name, character_class, level)
        self.alignment = alignment
        self.goals = goals
        self.faction = faction
        self.disposition = disposition
        self.knowledge = {}

    def add_knowledge(self, topic, knowledge):
        self.knowledge[topic] = knowledge




# Was generalized to BEING
#
# class NPC:
#     def __init__(self, name, npc_class, level, alignment, goals, faction, disposition):
#         self.name = name
#         self.npc_class = npc_class
#         self.level = level
#         self.alignment = alignment
#         self.goals = goals
#         self.faction = faction
#         self.disposition = disposition
#         self.knowledge = {}

#     def add_knowledge(self, topic, knowledge):
#         self.knowledge[topic] = knowledge
