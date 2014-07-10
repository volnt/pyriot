from pyriot.entity import Entity

class ChampionList(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.champions = [Champion(**c) for c in self.champions]

class Champion(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
    
