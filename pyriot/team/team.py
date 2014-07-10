from pyriot.entity import Entity

class Team(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.matchHistory = [MatchHistorySummary(**m) for m in self.matchHistory]
        self.teamStatDetails = [TeamStatDetail(**t) for t in self.teamStatDetails]

class Roster(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        self.memberList = [TeamMemberInfo(**m) for m in self.memberList]

class TeamStatsDetail(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)

class TeamMemberInfo(Entity):
    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)    
