import datetime
import time
import random
import requests
import numpy as np
import pandas as pd
import json
import validators
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

       
def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    

def scrape_olympics_websites(start_games, end_games, szn, df_olymp):
    # splitting the URL to prevent IDE issues
    url_1 = "https://"
    url_2 = "olympics.com/en/olympic-games/"

    # making a dataframe from the dictionary (2 rows, 38 columns for every olympics)
    df_olymp.index = df_olymp.index.astype(int)
    df_filter1 = df_olymp.loc[pd.to_numeric(start_games):pd.to_numeric(end_games)]
    df_filter2 = df_filter1.loc[(df_filter1['seasons'].astype(str) == f"['{szn}']") | (df_filter1['seasons'].astype(str) == f"['summer', 'winter']") ]
    
    #scraping operations here
    for city, season in enumerate(df_filter2['seasons']):
        # if the season is summer
        if ((('summer' in season)) & (szn == 'summer')):
            print(df_filter2.index[city]) # for year
            print(df_filter2['city'].iloc[city][0]) # for city
            url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
            
            req = Request(
            url= url_specific, 
            headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read()
            soup = BeautifulSoup(page, 'html.parser')
            soup_medalfilt = soup.find_all(title= "Gold")
            soup_filt = soup.find_all(class_ = "OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body")
            print(soup_medalfilt)
            time.sleep(random.uniform(0.05, 0.5))

        # if the season is winter
        elif ((('winter' in season)) & (szn == 'winter')):
            if (len(df_filter2['city'].iloc[city]) == 1):
                print(df_filter2.index[city]) # for year
                print(df_filter2['city'].iloc[city][0]) # for city
                url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
                
                req = Request(
                url= url_specific, 
                headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req).read()
                soup = BeautifulSoup(page, 'html.parser')
                soup_medalfilt = soup.find_all(title= "Gold")
                soup_filt = soup.find_all(class_ = "OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body")
                print(soup_medalfilt)
                time.sleep(random.uniform(0.05, 0.5))
            else:
                print(df_filter2.index[city]) # for year
                print(df_filter2['city'].iloc[city][1]) # winter olympic location (if 2 locations in a year) is always in the 2nd index location
                url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
                
                req = Request(
                url= url_specific, 
                headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req).read()
                soup = BeautifulSoup(page, 'html.parser')
                soup_medalfilt = soup.find_all(title= "Gold")
                soup_filt = soup.find_all(class_ = "OcsText-styles__StyledText-sc-bf256156-0 cjPVFu text--sm-body")
                print(soup_medalfilt)
                time.sleep(random.uniform(0.05, 0.5))
                

    