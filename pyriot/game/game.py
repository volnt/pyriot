from pyriot.entity import Entity

class Player(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class RawStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class Game(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.fellowPlayers = [Player(**p) for p in self.fellowPlayers]
        self.stats = RawStats(**self.stats)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class RecentGames(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.games = [Game(**g) for g in self.games]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
