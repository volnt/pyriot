from pyriot import PyRiot
from mock import patch

@patch.object(PyRiot, 'request')
def test_game_by_summoner(m_request):
    m_request.return_value = {
        "games": [{
            "fellowPlayers": [
                {
                    "championId": 106,
                    "teamId": 200,
                    "summonerId": 22588969
                },
                {
                    "championId": 54,
                    "teamId": 200,
                    "summonerId": 27627983
                },
                {
                    "championId": 43,
                    "teamId": 200,
                    "summonerId": 29401136
                },
                {
                    "championId": 67,
                    "teamId": 100,
                    "summonerId": 38839017
                },
                {
                    "championId": 28,
                    "teamId": 200,
                    "summonerId": 46622856
                },
                {
                    "championId": 157,
                    "teamId": 200,
                    "summonerId": 31080702
                },
                {
                    "championId": 96,
                    "teamId": 100,
                    "summonerId": 39212996
                },
                {
                    "championId": 99,
                    "teamId": 100,
                    "summonerId": 39584863
                },
                {
                    "championId": 13,
                    "teamId": 100,
                    "summonerId": 44072729
                }
            ],
            "gameType": "MATCHED_GAME",
            "stats": {
                "totalDamageDealtToChampions": 13545,
                "goldEarned": 10528,
                "item1": 3174,
                "totalDamageTaken": 21302,
                "item0": 3111,
                "TrueDamageDealtPlayer": 7326,
                "physicalDamageDealtPlayer": 5037,
                "TrueDamageDealtToChampions": 3175,
                "totalUnitsHealed": 8,
                "level": 17,
                "magicDamageDealtToChampions": 9427,
                "magicDamageDealtPlayer": 24024,
                "assists": 16,
                "magicDamageTaken": 10759,
                "numDeaths": 8,
                "totalTimeCrowdControlDealt": 256,
                "largestMultiKill": 1,
                "physicalDamageTaken": 10542,
                "win": True,
                "team": 100,
                "totalDamageDealt": 36388,
                "totalHeal": 3506,
                "item4": 3067,
                "item3": 3027,
                "item6": 2052,
                "minionsKilled": 24,
                "item5": 1026,
                "timePlayed": 1485,
                "physicalDamageDealtToChampions": 942,
                "championsKilled": 3,
                "goldSpent": 9170
            },
            "gameId": 1364797385,
            "ipEarned": 314,
            "spell1": 6,
            "teamId": 100,
            "spell2": 7,
            "gameMode": "ARAM",
            "mapId": 12,
            "level": 30,
            "invalid": False,
            "subType": "ARAM_UNRANKED_5x5",
            "createDate": 1394347941297,
            "championId": 31
        }],
        "summonerId": 24102751
    }

    api = PyRiot("euw", "mock-api-key")
    games = api.game_by_summoner(summonerId=123)

    assert len(games.games) == 1
    assert len(games.games[0].fellowPlayers) == 9
    assert games.games[0].gameType == "MATCHED_GAME"
    assert games.games[0].stats.win is True
    assert games.games[0].gameMode == "ARAM"
    assert games.games[0].championId == 31
    assert games.summonerId == 24102751
