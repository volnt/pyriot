from game import RecentGames
from summoner import Summoner, MasteryPages, RunePages
from stats import PlayerStatsSummaryList, RankedStats

return_dic = lambda m, r: {k: m(**v) for k, v in r.iteritems()}
return_obj = lambda m, r: m(**r)

ENDPOINTS = {
    "game_by_summoner": {
        "endpoint": "/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent",
        "mapping": RecentGames,
        "return": return_dic
    },
    "summoner_runes": {
        "endpoint": "/api/lol/{region}/v1.4/summoner/{summonerIds}/runes",
        "mapping": RunePages,
        "return": return_dic
    },
    "summoner_masteries": {
        "endpoint": "/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries",
        "mapping": MasteryPages,
        "return": return_dic
    },
    "summoner_name": {
        "endpoint": "/api/lol/{region}/v1.4/summoner/{summonerIds}/name",
        "mapping": str,
        "return": return_dic
    },
    "summoner": {
        "endpoint": "/api/lol/{region}/v1.4/summoner/{summonerIds}",
        "mapping": Summoner,
        "return": return_dic
    },
    "summoner_by_name": {
        "endpoint": "/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}",
        "mapping": Summoner,
        "return": return_dic
    },
    "stats_ranked": {
        "endpoint": "/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked",
        "mapping": RankedStats,
        "return": return_obj
    },
    "stats_summary": {
        "endpoint": "/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/summary",
        "mapping": PlayerStatsSummaryList,
        "return": return_obj
    },
}
