# Olympics Medals Comparison Python Application
# Made by: Bryan Hlavin and Tommaso Fazzi

import pandas as pd
import json
from olymp_funcs import check_for_json_database, scrape_olympics_websites
from user_questions import ask_for_years


# Step 0: Reading in JSON file preliminarily (contains basic Olypmics data)
f = open('olymp_games.json')
olymp_games = json.load(f)
df_olymp = pd.DataFrame.transpose(pd.DataFrame.from_dict(olymp_games['olympic_games_year']))


# Step 1-3: Checking to see if the file with all Olympics data is in the user's files - if not, then add it and scrape all websites
database_exists = check_for_json_database()
starting_games, ending_games, season = ask_for_years(olymp_games)
          
# Step 4-5: Begin Scraping Process - Index for resulting dataframe is 'Country'
df_total = scrape_olympics_websites(starting_games, ending_games, season, df_olymp)
print(df_total)

# The dataframe returned will have all the countries that have participated in at least one Olympic games
# between the two dates. If the country had not competed in any of the Olympic games, then the country will not show up.
# Countries that appear in one Olympic games but not others will have 'NaN' types for variables in the other columns.
# Countries are filtered alphabetically

# Step 6: Generating statistical tables based on dataframe


# Step 7: Calculating concluding statistics
