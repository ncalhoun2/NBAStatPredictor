from tqdm import tqdm

# format for the loading indicators in the console
# in your loop call 
# for i in consoleLoad(items, <String for title>)

def consoleLoad(items, text):
    return tqdm(items, desc=text, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]")