import datetime
import time
import random
from operator import index
import numpy as np
import pandas as pd
import json
import validators
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from scraping_funcs import bs_scrape

# Forcing the python console to show all columns of a resulting dataframe
pd.set_option('display.max_columns', None)

def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    
   

def scrape_olympics_websites(start_games, end_games, szn, df_olymp):
    print(F"Proceeding to scrape all olympics websites between (and including) the two years specified for the {szn} olympics.")

    # Splitting the URL to prevent IDE issues
    url_1 = "https://"
    url_2 = "olympics.com/en/olympic-games/"

    # Making a dataframe from the dictionary (2 rows, 38 columns for every olympics)
    df_olymp.index = df_olymp.index.astype(int)
    df_filter1 = df_olymp.loc[pd.to_numeric(start_games):pd.to_numeric(end_games)]
    df_filter2 = df_filter1.loc[(df_filter1['seasons'].astype(str) == f"['{szn}']") | (df_filter1['seasons'].astype(str) == f"['summer', 'winter']")]
    df_total_results = pd.DataFrame(columns = ['Country'])

    # Loop through each year's olympics
    for city, season in enumerate(df_filter2['seasons']):
        # If the season is summer
        if ((('summer' in season)) & (szn == 'summer')):
            url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
            location_in_series = df_filter2['city'].iloc[city][0]
            year_in_series = df_filter2.index[city]

            # Gathering countries and medal counts
            soup_countries_list, soup_medals_list = bs_scrape(url_specific, location_in_series)

            # Placing values in dataframe
            df_total_results = place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results)
           
        # If the season is winter
        elif ((('winter' in season)) & (szn == 'winter')):
            if (len(df_filter2['city'].iloc[city]) == 1):
                url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][0]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
                location_in_series = df_filter2['city'].iloc[city][0]
                year_in_series = df_filter2.index[city]
                        
                # Gathering countries and medal counts
                soup_countries_list, soup_medals_list = bs_scrape(url_specific, location_in_series)

                # Placing values in dataframe
                df_total_results = place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results)

            else:
                url_specific = f"{url_1}{url_2}{df_filter2['city'].iloc[city][1]}-{df_filter2.index[city]}/medals?displayAsWebViewlight=true&displayAsWebView=true"
                location_in_series = df_filter2['city'].iloc[city][1]
                year_in_series = df_filter2.index[city]
                
                # Gathering countries and medal counts
                soup_countries_list, soup_medals_list = bs_scrape(url_specific, location_in_series)

                # Placing values in dataframe
                df_total_results = place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results)
                
    # making all "-" or " " values into "0" values
    # Setting 'Country' as the index value
    df_total_results.set_index('Country', inplace = True)            
    return df_total_results


def place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results):
     
     # Adding columns to the total dataframe for each year's olympic medal count
     df_total_results[f'{year_in_series}_gold'] = ""
     df_total_results[f'{year_in_series}_silver'] = ""
     df_total_results[f'{year_in_series}_bronze'] = ""
     df_total_results[f'{year_in_series}_total'] = ""
                
     # if the country in the medal list does not not appear yet, add it and add the medals - if it does appear, match it with the right row and add in the variabls for the new medals
     for i in range(len(soup_countries_list)):
        if soup_countries_list[i-1] in df_total_results['Country'].values:
            # find the exact row it is in, and put the 4 values for each medal placement there
            country_match = df_total_results.index[(df_total_results['Country'] == soup_countries_list[i-1])].to_list()
            df_total_results.loc[country_match[0], f'{year_in_series}_gold'] = soup_medals_list[4*(i-1)]
            df_total_results.loc[country_match[0], f'{year_in_series}_silver'] = soup_medals_list[4*(i-1)+1]
            df_total_results.loc[country_match[0], f'{year_in_series}_bronze'] = soup_medals_list[4*(i-1)+2]
            df_total_results.loc[country_match[0], f'{year_in_series}_total'] = soup_medals_list[4*(i-1)+3]
                        
        else:
            df_total_results = df_total_results.append({'Country': soup_countries_list[i-1], 
                                                        f'{year_in_series}_gold': soup_medals_list[4*(i-1)],   \
                                                        f'{year_in_series}_silver': soup_medals_list[4*(i-1)+1], \
                                                        f'{year_in_series}_bronze': soup_medals_list[4*(i-1)+2], \
                                                        f'{year_in_series}_total': soup_medals_list[4*(i-1)+3]}, ignore_index = True)
     
     # Loop pauser just in case the website freaks out from scraping too fast
     time.sleep(random.uniform(0.10, 0.85))
     
     return df_total_results    