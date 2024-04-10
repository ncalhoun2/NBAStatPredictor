from players import get_players_list

#get table of all players stats for the who retiered after a certain year

def get_all_players_stats(year):
    # player names to get stats for
    player_names = get_players_list(year)
    
    for player_name in tqdm(player_names, desc="Players stats loading...", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
        time.sleep(5)
        player_url = get_player_url(player_name)
        get_player_years_played(player_url)
    return

get_all_players_stats(2002)