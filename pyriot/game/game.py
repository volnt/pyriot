from pyriot.entity import Entity

class Player(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class RawStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class Game(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.fellowPlayers = [Player(**p) for p in self.fellowPlayers]
        self.stats = RawStats(**self.stats)

class RecentGames(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.games = [Game(**g) for g in self.games]
    
