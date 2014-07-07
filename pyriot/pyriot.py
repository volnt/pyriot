import requests
from game import RecentGames
from summoner import Summoner, MasteryPages, RunePages

class RiotException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class PyRiot(object):
    
    base_url = "https://{region}.api.pvp.net"
    available_region = ("br", "euw", "eune", "kr", "lan",
                        "las", "na", "oce", "ru", "tr")

    def __init__(self, region, api_key):
        if region not in self.available_region:
            raise RiotException("Region '{}' does not exists.".format(region))
        self.region = region
        self.api_key = api_key

    def request(self, endpoint, **kwargs):
        kwargs["region"] = self.region
        kwargs["api_key"] = self.api_key

        url = self.base_url + endpoint + "?api_key={api_key}"

        response = requests.get(url.format(**kwargs))

        if response.ok:
            return response.json()
        raise RiotException("Request failed.")

    def game_by_summoner(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent"
        mapping = RecentGames

        return mapping(**self.request(endpoint, **kwargs))

    def summoner_runes(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.4/summoner/{summonerIds}/runes"
        mapping = RunePages

        response = self.request(endpoint, **kwargs)
        return {key: mapping(**value) for key, value in response.iteritems()}

    def summoner_masteries(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries"
        mapping = MasteryPages

        response = self.request(endpoint, **kwargs)
        return {key: mapping(**value) for key, value in response.iteritems()}

    def summoner_name(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.4/summoner/{summonerIds}/name"

        return self.request(endpoint, **kwargs)

    def summoner(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.4/summoner/{summonerIds}"
        mapping = Summoner

        response = self.request(endpoint, **kwargs)
        return {key: mapping(**value) for key, value in response.iteritems()}

    def summoner_by_name(self, **kwargs):
        endpoint = "/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}"
        mapping = Summoner

        response = self.request(endpoint, **kwargs)
        return {key: mapping(**value) for key, value in response.iteritems()}
