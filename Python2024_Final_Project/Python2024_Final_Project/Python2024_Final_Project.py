# Olympics Medals Comparison Python Application
# Made by: Bryan Hlavin and Tommaso Fazzi

import datetime
import time
import random
import requests
import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from olymp_funcs import is_valid_olympic_year, scrape_olympics_websites


valid_games = False

# Steps Involved
# ---------------------
# Step 0: 
# Reading in JSON file preliminarily (contains basic Olypmics data)
f = open('olymp_games.json')
olymp_games = json.load(f)
df_olymp = pd.DataFrame.from_dict(olymp_games['olympic_games_year'])

# Step 1-3:
# Prompt the user to ask which olympics to start with and end with 
print("Please type in which Olympic Games you wish to START this comparison with.")

# Asking for starting year (using dictionary processes to start)
while valid_games == False:
    starting_games = input("Enter year of Olympic Games: ")
    if any(x.isalpha() for x in starting_games):
        print("You have not imputted a year of a valid olympic games. Please input again: ")
    else:
        if (is_valid_olympic_year(starting_games, olymp_games) == True):
             if (len(olymp_games['olympic_games_year'][f'{starting_games}']['seasons'])) > 1:
                print(f"The year {starting_games} had both winter and summer games. Please specify which season you would like to see.")
                print("Type 's' or 'summer' for the Summer Olympics, and 'w' or 'winter' for Winter Olympics")
                szn = input("Enter season: ")
                if szn.lower() in ["s","summer"]:
                    print(f"You have selected the summer olympics for {starting_games} in {olymp_games['olympic_games_year'][f'{starting_games}']['city'][0]} as a starting point.")
                    szn = "summer"
                    valid_games= True
                elif szn.lower() in ["w","winter"]: 
                    print(f"You have selected the winter olympics for {starting_games} in {olymp_games['olympic_games_year'][f'{starting_games}']['city'][1]} as a starting point.")
                    szn = "winter"
                    valid_games = True
                else:
                    print("You have not imputted a valid season. Please start over.")
             else:
                print(f"The year {starting_games} has only {olymp_games['olympic_games_year'][f'{starting_games}']['seasons'][0]} games.")
                print(f"This means you have selected the {olymp_games['olympic_games_year'][f'{starting_games}']['seasons'][0]} olympics for {starting_games} in {olymp_games['olympic_games_year'][f'{starting_games}']['city']} as a starting point.")
                szn = f"{olymp_games['olympic_games_year'][f'{starting_games}']['seasons'][0]}"
                valid_games = True
        else:
            print("You have not imputted a year of a valid olympic games. Please input again: ")
      

# Asking for ending year
valid_games = False
while valid_games == False:
    ending_games = input("Please type in which Olympic Games you wish to END this comparison with: ")
    if any(x.isalpha() for x in ending_games):
        print("You have not imputted a year of a valid olympic games. Please input again: ")
    else:
        if (is_valid_olympic_year(ending_games, olymp_games) == True & (pd.to_numeric(ending_games) > pd.to_numeric(starting_games))):
             if szn in olymp_games['olympic_games_year'][f'{ending_games}']['seasons']:
                 print(f"There was an olympic games in {ending_games} for {szn}.")
                 valid_games = True
             else:
                print("You have not imputted a year of a valid olympic games. Please input again: ")
        else:
             print("You have not imputted a year of a valid olympic games. Please input again: ")
 

# ---------------------
# Step 4:           
# Begin Scraping Process
print(F"Proceeding to scrape all olympics websites between (and including) the two years for the {szn} olympics.")
df_total = scrape_olympics_websites(starting_games, ending_games, szn, df_olymp)


# make this web scrape into a function that converts into proper data format for data fraome
# Load the 2016 website medal count
#req_2016 = Request(
#    url='https://olympics.com/en/olympic-games/paris-2024/medals?displayAsWebViewlight=true&displayAsWebView=true', 
#    headers={'User-Agent': 'Mozilla/5.0'}
#)
#page = urlopen(req_2016).read()
#soup = BeautifulSoup(page, 'html.parser')
#soup_medalfilt = soup.find_all(title= "Gold")
#soup_filt = soup.find_all(class_ = "OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body")
#print(soup_medalfilt)
#time.sleep(random.uniform(0.05, 0.5))

# Load the 2020 website medal count
#req_2020 = Request(
#    url='https://olympics.com/en/olympic-games/tokyo-2020/medals?displayAsWebViewlight=true&displayAsWebView=true', 
#    headers={'User-Agent': 'Mozilla/5.0'}
#)
#time.sleep(random.uniform(0.05, 0.5))
#age = urlopen(req_2020).read()
#soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())
#time.sleep(random.uniform(0.05, 0.5))

# Load the 2024 website medal count
#req_2024 = Request(
#    url='https://olympics.com/en/olympic-games/rio-2016/medals?displayAsWebViewlight=true&displayAsWebView=true', 
#    headers={'User-Agent': 'Mozilla/5.0'}
#)
#page = urlopen(req_2024).read()
#soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

# Filter out the information needed on the page (Beautify it)
# Make a data frame with the remaining information (try to combine departures and arrivals)
# Filter out flights by delay time (add "tiers" for delayed-ness)
# With the remaining filtered data, make charts, graphs, etc. 

