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
from user_questions import ask_for_years


# --------------------
# Step 0: Reading in JSON file preliminarily (contains basic Olypmics data)
f = open('olymp_games.json')
olymp_games = json.load(f)
df_olymp = pd.DataFrame.transpose(pd.DataFrame.from_dict(olymp_games['olympic_games_year']))

# Step 1-3: Prompt the user to ask which olympics to start with and end with 
starting_games, ending_games, season = ask_for_years(olymp_games)
          
# Step 4-5: Begin Scraping Process
df_total = scrape_olympics_websites(starting_games, ending_games, season, df_olymp)


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

