import datetime
import time
import random
from operator import index
import requests
import numpy as np
import pandas as pd
import json
import validators
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

       
pd.set_option('display.max_columns', None)

def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    


def scrape_olympics_websites(start_games, end_games, szn, df_olymp):
    
    print(F"Proceeding to scrape all olympics websites between (and including) the two years specified for the {szn} olympics.")

    # splitting the URL to prevent IDE issues
    url_1 = "https://"
    url_2 = "olympics.com/en/olympic-games/"

    # making a dataframe from the dictionary (2 rows, 38 columns for every olympics)
    df_olymp.index = df_olymp.index.astype(int)
    df_filter1 = df_olymp.loc[pd.to_numeric(start_games):pd.to_numeric(end_games)]
    df_filter2 = df_filter1.loc[(df_filter1['seasons'].astype(str) == f"['{szn}']") | (df_filter1['seasons'].astype(str) == f"['summer', 'winter']")]
    df_total_results = pd.DataFrame(columns = ['Country'])

    # scraping operations here
    for city, season in enumerate(df_filter2['seasons']):
        # if the season is summer
        if ((('summer' in season)) & (szn == 'summer')):
            print(df_filter2.index[city]) # for year
            print(df_filter2['city'].iloc[city][0]) # for city
            url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
            
            # parsing
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
                url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
                
                # Parsing
                req = Request(
                url= url_specific, 
                headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req).read()
                soup = BeautifulSoup(page, 'html.parser')
                
                # Adding columns to the total dataframe for each year's olympic medal count
                df_total_results[f'{df_filter2.index[city]}_gold'] = ""
                df_total_results[f'{df_filter2.index[city]}_silver'] = ""
                df_total_results[f'{df_filter2.index[city]}_bronze'] = ""
                df_total_results[f'{df_filter2.index[city]}_total'] = ""

                # Gathering countries and medal counts
                soup_countries_list = [tag.get_text() for tag in list(soup.find_all('span', attrs = {'data-cy':'country-name'}))]
                soup_medals_list = [tag.get_text() for tag in list(soup.find_all('span', attrs = {'data-cy':'ocs-text-module'}))]

                # if the country in the medal list does not not appear yet, add it and add the medals - if it does appear, match it with the right row and add in the variabls for the new medals
                for i in range(len(soup_countries_list)):
                    if soup_countries_list[i-1] in df_total_results['Country'].values:
                        # find the exact row it is in, and put the 4 values for each medal placement there
                        #print(df_total_results.index[df_total_results['Country']==soup_countries_list[i-1]].tolist())
                        print("match")
                    else:
                        df_total_results = df_total_results.append({'Country': soup_countries_list[i-1], 
                                                                    f'{df_filter2.index[city]}_gold': soup_medals_list[4*(i-1)+1],   \
                                                                    f'{df_filter2.index[city]}_silver': soup_medals_list[4*(i-1)+2], \
                                                                    f'{df_filter2.index[city]}_bronze': soup_medals_list[4*(i-1)+3], \
                                                                    f'{df_filter2.index[city]}_total': soup_medals_list[4*(i-1)+4]}, ignore_index = True)

                        #print(df_total_results.index[df_total_results['Country']==soup_countries_list[i-1]].tolist())

                #lengths of countries lists in 2002 and 2006 differ, so errors are generated- need to fix
                #df_results.insert(0, 'Country', soup_countries_list, True)
                #df_results[f'{df_filter2.index[city]}_gold'] = soup_medals_list[0::4]
                #df_results[f'{df_filter2.index[city]}_silver'] = soup_medals_list[1::4]
                #df_results[f'{df_filter2.index[city]}_bronze'] = soup_medals_list[2::4]
                #df_results[f'{df_filter2.index[city]}_total'] = soup_medals_list[3::4]

                # putting them as the index for the data frame
                #for i in range(soup_countries_list):
                #    if df_results.index.isin(soup_countries_list[i-1]):
                #        # find the exact row it is in, and put the 4 values for each medal placement there
                #    else:
                #        # add a new row for medal placement and add the index for the country in questions
                        
                #print(soup_medalfilt2)
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
      
    # printing everthing I can 
    df_total_results.set_index('Country', inplace = True)            
    print(df_total_results)
    return df_total_results

    