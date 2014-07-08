from pyriot.entity import Entity

class PlayerStatsSummaryList(Entity):
    def __init__(self, **kwargs): 
        Entity.__init__(self, **kwargs)
        self.playerStatSummaries = [PlayerStatsSummary(**stats) for stats 
                                    in self.playerStatSummaries]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class PlayerStatsSummary(Entity):
    def __init__(self, **kwargs): 
        Entity.__init__(self, **kwargs)
        self.aggregatedStats = AggregatedStats(**self.aggregatedStats)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class RankedStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.champions = [ChampionStats(**champion) for champion in self.champions]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class ChampionStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.stats = AggregatedStats(**self.stats)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class AggregatedStats(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
