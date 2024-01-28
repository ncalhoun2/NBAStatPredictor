from src.data_retreival.player_stats import get_player_url

# test player url retreival
def test_player_url_lavine():
    result = get_player_url("Zach LaVine")
    player_url = "https://www.basketball-reference.com/players/l/lavinza01.html"
    assert result == player_url, "Incorrect player url"

def test_player_url_coby():
    result = get_player_url("Coby White")
    player_url = "https://www.basketball-reference.com/players/w/whiteco01.html"
    assert result == player_url, "Incorrect player url"