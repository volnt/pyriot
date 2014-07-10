import requests
from endpoints import ENDPOINTS

class RiotException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class PyRiot(object):
    
    base_url            = "https://{region}.api.pvp.net"
    available_region    = ("br", "euw", "eune", "kr", "lan",
                           "las", "na", "oce", "ru", "tr")
    endpoints           = ENDPOINTS

    def __init__(self, region, api_key):
        if region not in self.available_region:
            raise RiotException("Region '{}' does not exist.".format(region))
        self.region = region
        self.api_key = api_key
        
    def request(self, endpoint, **kwargs):
        kwargs["region"]        = self.region
        kwargs["api_key"]       = self.api_key
        fmt_url                 = self.base_url + endpoint + "?api_key={api_key}"

        try:
            response = requests.get(fmt_url.format(**kwargs))
        except KeyError as e:
            raise RiotException("An argument is missing : {}".format(e))

        if not response.ok:
            raise RiotException("Request failed.")
        return response.json()

    def __getattr__(self, attr):
        if attr in self.endpoints:
            endpoint    = self.endpoints[attr]["endpoint"]
            mapping     = self.endpoints[attr]["mapping"]
            ret         = self.endpoints[attr]["return"]
            return lambda *a, **k: ret(mapping, self.request(endpoint, **k))
        else:
            raise RiotException("Endpoint '{}' does not exist.".format(name))
