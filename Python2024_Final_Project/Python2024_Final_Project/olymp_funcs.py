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
    df_olymp.index = df_olymp.index.astype(int)
    df_filter1 = df_olymp.loc[pd.to_numeric(start_games):pd.to_numeric(end_games)]
    df_filter2 = df_filter1.loc[(df_filter1['seasons'].astype(str) == f"['{szn}']") | (df_filter1['seasons'].astype(str) == f"['summer', 'winter']") ]
    
    #scraping operations here
    for season in df_filter2['seasons']:
        # if the season is summer
        print(season)
        print(f"Value: {season}, Type: {type(season)}")
        if ((('summer' in season)) & (szn == 'summer')):
            print("Doable for summer!")
 
        # if the season is winter
        elif ((('winter' in season)) & (szn == 'winter')):
            print("Doable for winter!")
            
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
    

        