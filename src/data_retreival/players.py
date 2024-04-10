import string
import pandas as pd
from tqdm import tqdm
import time


# players list for names starting with a is here: https://www.basketball-reference.com/players/a/
# change the last letter for the list of that letter players/a/ -> players/b/

def get_players_list(retirement_year):
    # Get the alphabet letters in lowercase
    alphabet = string.ascii_lowercase
    
    # Initialize an empty list to store player DataFrames
    all_players = []
    
    # Iterate through each letter in the alphabet to fetch player data
    for letter in tqdm(alphabet, desc="Players loading...", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
        time.sleep(5)
        url = "https://www.basketball-reference.com/players/{letter}/"
        players_table = pd.read_html(url)[0]
        
        # Filter players based on retirement year
        players_table['To'] = pd.to_numeric(players_table['To'], errors='coerce')  # Convert 'To' column to numeric
        active_players = players_table[players_table['To'] > retirement_year]
        
        # Append the filtered DataFrame to the list
        all_players.append(active_players)

    # Concatenate all player DataFrames into a single DataFrame
    all_players_df = pd.concat(all_players, ignore_index=True)

    print(all_players_df)
    
    return all_players_df





