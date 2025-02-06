# Olympics Medals Comparison Python Application
# Made by: Bryan Hlavin and Tommaso Fazzi

import pandas as pd
import json
from olymp_funcs import check_for_json_database, scrape_olympics_websites
from user_questions import ask_for_year_or_country
from graphing_func import plot_medal_histogram


# Step 0: Reading in JSON file preliminarily (contains basic Olypmics data)
f = open('olymp_games.json')
olymp_games = json.load(f)
df_olymp = pd.DataFrame.transpose(pd.DataFrame.from_dict(olymp_games['olympic_games_year']))


# Step 1: Checking to see if the file with all Olympics data is in the user's files
database_exists = check_for_json_database()
          
# Step 2: Begin Scraping Process if needed - Index for resulting dataframe is 'Country'
df_total = scrape_olympics_websites(df_olymp)

# This is the dataframe with every result
print(df_total)

# Step 3-4: Prompt User on What They Want to See and Make Graphs
ask_for_year_or_country(olymp_games, df_total)
plot_medal_histogram(df_total= any, szn= any, year= any, country= any)

