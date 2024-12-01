import datetime
import time
import random
import requests
import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

       
def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    

def scrape_olympics_websites(start_games, end_games, szn, df_olymp):
    # making a dataframe from the dictionary (2 rows, 38 columns for every olympics)
    print(df_olymp)
    #df_filtered = pd.DataFrame.from_dict(df_olymp['olympic_games_year'])

    # making a shorthand list to simplify things later
    #list_olympics = list(games_json['olympic_games_year'].keys())

    #df_valid_olympics = filter((games_json['olympic_games_year'].keys()>= f'{start_games}') & (games_json['olympic_games_year'].keys() <= end_games))
    #print(df_valid_olympics)
    

    # cycle through the dataframe, scraping each website
    #for 
    #req = Request(url=f'https://olympics.com/en/olympic-games/paris-2024/medals?displayAsWebViewlight=true&displayAsWebView=true', 
#    headers={'User-Agent': 'Mozilla/5.0'}
#))



    
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
    

        