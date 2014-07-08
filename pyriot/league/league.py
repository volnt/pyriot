from pyriot.entity import Entity

class League(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.entries = [LeagueEntry(**e) for e in self.entries]

class LeagueEntry(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.miniSeries = MiniSeries(self.miniSeries)

class MiniSeries(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
