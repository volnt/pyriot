from pyriot import PyRiot
from mock import patch

@patch.object(PyRiot, 'request')
def test_champion(m_request):
    m_request.return_value = {
        "champions": [
        {
            "botMmEnabled": False,
            "id": 266,
            "rankedPlayEnabled": True,
            "botEnabled": False,
            "active": True,
            "freeToPlay": False
        }, 
        {
            "botMmEnabled": False,
            "id": 103,
            "rankedPlayEnabled": True,
            "botEnabled": False,
            "active": True,
            "freeToPlay": False
        },
        {
            "botMmEnabled": False,
            "id": 84,
            "rankedPlayEnabled": True,
            "botEnabled": False,
            "active": True,
            "freeToPlay": False
        }
    ]}

    api = PyRiot("euw", "mock-api-key")
    champions = api.champion()

    assert len(champions.champions) == 3
    assert champions.champions[0].botMmEnabled is False
    assert champions.champions[1].id == 103
    assert champions.champions[2].rankedPlayEnabled is True

@patch.object(PyRiot, 'request')
def test_champion_id(m_request):
    m_request.return_value = {
        "botMmEnabled": True,
        "id": 1,
        "rankedPlayEnabled": True,
        "botEnabled": True,
        "active": True,
        "freeToPlay": False
    }

    api = PyRiot("euw", "mock-api-key")
    champion = api.champion_id(id=1)

    assert champion.id == 1
    assert champion.active is True
    assert champion.freeToPlay is False
