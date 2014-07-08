from game import RecentGames
from league import League
from summoner import Summoner, MasteryPages, RunePages
from stats import PlayerStatsSummaryList, RankedStats

return_dic      = lambda m, r: {k: m(**v) for k, v in r.iteritems()}
return_diclst   = lambda m, r: {k: [m(**v) for v in l] for k, l in r.iteritems()}
return_obj      = lambda m, r: m(**r)
return_lst      = lambda m, r: [m(**l) for l in r]

ENDPOINTS = {

    # Champion module endpoints

    "champion": {
        "endpoint": "/api/lol/{region}/v1.2/champion",
        "mapping": None,
        "return": return_obj
    },
    "champion_id": {
        "endpoint": "/api/lol/{region}/v1.2/champion/{id}",
        "mapping": None,
        "return": return_obj
    },

    # Game module endpoints

    "game_by_summoner": {
        "endpoint": "/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent",
        "mapping": RecentGames,
        "return": return_dic
    },
    
    # League module endpoints

    "league_by_summoner": {
        "endpoint": "/api/lol/{region}/v2.4/league/by-summoner/{summonerIds}",
        "mapping": League,
        "return": return_diclst
    },
    "league_by_summoner_entry": {
        "endpoint": "/api/lol/{region}/v2.4/league/by-summoner/{summonerIds}/entry",
        "mapping": League,
        "return": return_diclst
    },
    "league_by_team": {
        "endpoint": "/api/lol/{region}/v2.4/league/by-team/{teamIds}",
        "mapping": League,
        "return": return_diclst
    },
    "league_by_team_entry": {
        "endpoint": "/api/lol/{region}/v2.4/league/by-team/{teamIds}/entry",
        "mapping": League,
        "return": return_diclst
    },
    "league_challenger": {
        "endpoint": "/api/lol/{region}/v2.4/league/challenger",
        "mapping": League,
        "return": return_obj
    },    
    
    # Static data module endpoints

    "static_data_champion": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/champion",
        "mapping": None,
        "return": return_obj
    },
    "static_data_champion_id": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/champion/{id}",
        "mapping": None,
        "return": return_obj
    },
    "static_data_item": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/item",
        "mapping": None,
        "return": return_obj
    },
    "static_data_item_id": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/item/{id}",
        "mapping": None,
        "return": return_obj
    },
    "static_data_mastery": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/mastery",
        "mapping": None,
        "return": return_obj
    },
    "static_data_mastery_id": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/mastery/{id}",
        "mapping": None,
        "return": return_obj
    },
    "static_data_realm": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/realm",
        "mapping": None,
        "return": return_obj
    },
    "static_data_rune": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/rune",
        "mapping": None,
        "return": return_obj
    },
    "static_data_rune_id": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/rune/{id}",
        "mapping": None,
        "return": return_obj
    },
    "static_data_summoner_spell": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/summoner-spell",
        "mapping": None,
        "return": return_obj
    },
    "static_data_summoner_spell_id": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/summoner-spell/{id}",
        "mapping": None,
        "return": return_obj
    },
    "static_data_versions": {
        "endpoint": "/api/lol/static-data/{region}/v1.2/versions",
        "mapping": str,
        "return": return_lst
    },
        
    # Summoner module endpoints

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
    
    # Stats module endpoints

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
    
    # Team module endpoints

    "teeam_by_summoner": {
        "endpoint": "/api/lol/{region}/v2.3/team/by-summoner/{summonerIds}",
        "mapping": None,
        "return": return_diclst
    },
    "team": {
        "endpoint": "/api/lol/{region}/v2.3/team/{teamIds}",
        "mapping": None,
        "return": return_dic
    }
}
