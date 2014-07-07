from pyriot.entity import Entity

class Summoner(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class MasteryPages(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.pages = [MasteryPage(**p) for p in self.pages]

class MasteryPage(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.masteries = [Mastery(**m) for m in self.masteries]

class Mastery(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
    
class RunePages(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.pages = [RunePage(**p) for p in self.pages]

class RunePage(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.slots = [RuneSlot(**m) for m in self.slots]

class RuneSlot(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
    
