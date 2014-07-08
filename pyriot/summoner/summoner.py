from pyriot.entity import Entity

class Summoner(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class MasteryPages(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.pages = [MasteryPage(**p) for p in self.pages]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class MasteryPage(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.masteries = [Mastery(**m) for m in self.masteries]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class Mastery(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
class RunePages(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.pages = [RunePage(**p) for p in self.pages]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class RunePage(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.slots = [RuneSlot(**m) for m in self.slots]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class RuneSlot(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
