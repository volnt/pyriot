# pyriot

/!\ Work In Progress

Python wrapper for the League of Legends API.

The API documentation can be found here : [https://developer.riotgames.com/api/methods](https://developer.riotgames.com/api/methods).

## Installation

You can install the package using pip. (pip install -e .)

## Usage

```python
from pyriot import PyRiot
api = PyRiot("na", "your-api-key") # get your api key from you developer account
api.summoner_by_name(summonerNames="RiotSchmick")
# Return Value : {u'riotschmick': <pyriot.summoner.summoner.Summoner object at 0x11e6f50>}
```

The pyriot.summoner.summoner.Summoner object has all the attributes described in the documentation. (id, name, profileIconId, etc..)

If you forget to put the proper api key you will get a RiotException saying "Request failed".

## TODO

* champion module
* league module
* lol-static-data module
* stats module
* team module
* proper documentation