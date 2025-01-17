from genericpath import isfile
from math import fabs
import time
import random
import numpy as np
import pandas as pd
import os
import json
from scraping_funcs import bs_scrape

# Forcing the python console to show all columns of a resulting dataframe
pd.set_option('display.max_columns', None)

def check_for_json_database():
    # check to see if a file exists - if it doesn't then make it and perform all the scraping actions in the below function
    if os.path.isfile("olymp_database.json"):
        print("The database for all olympic games exists...continuing without scraping any websites...")
        return True
    else:
        print("The database for all olympic games does not exists...generating new file....")
        with open("olymp_database.json",'w') as f:
            f.write("{}")
            f.close()
        print("New database for olympics generated. Scraping websites...")
        return False
        

def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    
   

def scrape_olympics_websites(df_olymp):
    print(f'Proceeding to scrape all olympics websites....')
    print(' ')
    
    # Making an empty json dictionary
    with open("olymp_database.json", 'r') as f:
        olymp_data = json.load(f)
        olymp_data = {}

    # Splitting the URL to prevent IDE issues
    url_1 = 'https://'
    url_2 = 'olympics.com/en/olympic-games/'

    # Making a dataframe from the dictionary (2 rows, 38 columns for every olympics)
    df_olymp.index = df_olymp.index.astype(int)
    df_filter1 = df_olymp.loc[pd.to_numeric(1896):pd.to_numeric(2024)]
    #df_filter2 = df_filter1.loc[(df_filter1['seasons'].astype(str) == f"['{szn}']") | (df_filter1['seasons'].astype(str) == f"['summer', 'winter']")]
    
    df_total_results = pd.DataFrame(columns = ['Country'])

    # Loop through each year's olympics
    for index, city in enumerate(df_filter1['city']):
        for loc in city:
            location_in_series = loc
            year_in_series = df_filter1.index[index]
            season = df_filter1['seasons'].iloc[index][city.index(loc)]
            print(f"Getting results: {year_in_series} - {location_in_series} - {season}")
            url_specific = f"{url_1}{url_2}{location_in_series}-{year_in_series}/medals?displayAsWebViewlight=true&displayAsWebView=true"

            # Gathering countries and medal counts
            soup_countries_list, soup_medals_list = bs_scrape(url_specific, location_in_series)

            # Placing values in dataframe
            df_total_results = place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results)
            
            # Placing values in json file
            json_database_data = {
                                f"{location_in_series}-{year_in_series}": 
                                {
                                    "year": f"{year_in_series}",
                                    "city": f"{location_in_series}",
                                    "season": f"{season}"
                                }
                                }
            olymp_data.update(json_database_data)

            with open("olymp_database.json", 'w') as f:
                json.dump(olymp_data, f, indent=4)
                
    # making all "-" values into "0" values, and making " " values into "NaN" values
    df_total_results = df_total_results.where(df_total_results != '-', '0')
    df_total_results = df_total_results.where(df_total_results != '', np.nan)

    # Setting 'Country' as the index value
    df_total_results.set_index('Country', inplace = True)
    
    return df_total_results.sort_values('Country')


def place_values_in_dataframe(soup_countries_list, soup_medals_list, year_in_series, df_total_results):
     # Adding columns to the total dataframe for each year's olympic medal count
     df_total_results[f'{year_in_series}_gold'] = ''
     df_total_results[f'{year_in_series}_silver'] = ''
     df_total_results[f'{year_in_series}_bronze'] = ''
     df_total_results[f'{year_in_series}_total'] = ''
                
     # If the country in the medal list does not not appear yet, add it and add the medals - if it does appear, match it with the right row and add in the variabls for the new medals
     for i in range(len(soup_countries_list)):
        if soup_countries_list[i-1] in df_total_results['Country'].values:
            # Find the exact row it is in, and put the 4 values for each medal placement there
            country_match = df_total_results.index[(df_total_results['Country'] == soup_countries_list[i-1])].to_list()
            df_total_results.loc[country_match[0], f'{year_in_series}_gold'] = soup_medals_list[4*(i-1)]
            df_total_results.loc[country_match[0], f'{year_in_series}_silver'] = soup_medals_list[4*(i-1)+1]
            df_total_results.loc[country_match[0], f'{year_in_series}_bronze'] = soup_medals_list[4*(i-1)+2]
            df_total_results.loc[country_match[0], f'{year_in_series}_total'] = soup_medals_list[4*(i-1)+3]
                        
        else:
            new_row = pd.DataFrame([{
                'Country': soup_countries_list[i-1],
                'Medals': soup_medals_list[i-1],
                'Year': year_in_series
                }])
            df_total_results = pd.concat([df_total_results, new_row], ignore_index=True)

     
     # Loop pauser just in case the website freaks out from scraping too fast
     time.sleep(random.uniform(0.10, 0.85))
     
     return df_total_results    