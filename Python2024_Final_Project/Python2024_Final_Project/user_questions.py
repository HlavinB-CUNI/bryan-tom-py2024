import pandas as pd
from olymp_funcs import is_valid_olympic_year, is_valid_olympic_country
from graphing_func import plot_medal_histogram

# Prompt the user to ask which olympics to start with and end with 
def ask_for_year_or_country(olymp_games, df_total):
    valid_req = False
        
    while valid_req == False:
        
        print("Do you wish to see a country's medal statistics, or the top 10 results for a specific Olympic games? Type country or year for either.")
        user_request = input("Enter request: ")
        valid_answer = False
        
        # If the user selects a specific year
        if user_request.lower() in ["year","yr", "y"]:
        # If the user selects a specific year
            while valid_answer == False:
                games_year = input("Enter year of Olympic Games: ")
                if any(x.isalpha() for x in games_year):
                    print("You have not imputted a year of a valid olympic games. Please input again: ")
                else:
                    if (is_valid_olympic_year(games_year, olymp_games) == True):
                        if (len(olymp_games['olympic_games_year'][f'{games_year}']['seasons'])) > 1:
                            print(f"The year {games_year} had both winter and summer games. Please specify which season you would like to see.")
                            print("Type 's' or 'summer' for the Summer Olympics, and 'w' or 'winter' for Winter Olympics")
                            szn = input("Enter season: ")
                            if szn.lower() in ["s","summer"]:
                                print(f"You have selected the summer olympics for {games_year} in {olymp_games['olympic_games_year'][f'{games_year}']['city'][0]}.")
                                szn = "summer"
                                plot_medal_histogram(df_total, szn, games_year, country=None)
                                valid_answer = True
                            elif szn.lower() in ["w","winter"]: 
                                print(f"You have selected the winter olympics for {games_year} in {olymp_games['olympic_games_year'][f'{games_year}']['city'][1]}.")
                                szn = "winter"
                                plot_medal_histogram(df_total, szn, games_year, country=None)
                                valid_answer = True
                            else:
                                print("You have not imputted a valid season. Please start over.")
                                valid_answer = False
                        else:
                            print(f"The year {games_year} has only {olymp_games['olympic_games_year'][f'{games_year}']['seasons'][0]} games.")
                            print(f"This means you have selected the {olymp_games['olympic_games_year'][f'{games_year}']['seasons'][0]} olympics for {games_year} in {olymp_games['olympic_games_year'][f'{games_year}']['city']}.")
                            szn = f"{olymp_games['olympic_games_year'][f'{games_year}']['seasons'][0]}"
                            plot_medal_histogram(df_total, szn, games_year, country=None)
                    else:
                        print("You have not imputted a year of a valid olympic games. Please input again: ")
                        valid_answer = False
            valid_req = True

        # If the user selects a specific country
        elif user_request.lower() in ["country","cnt", "c"]:                
            while valid_answer == False:                
                games_country = input("Enter Country: ")
                if (is_valid_olympic_country(games_country, df_total) == True):
                    print("Type 's' or 'summer' for the Summer Olympics, and 'w' or 'winter' for Winter Olympics")
                    szn = input("Enter season: ")
                    if szn.lower() in ["s","summer"]:
                        print(f"You have selected the summer olympics for {games_country}.")
                        szn = "summer"
                        valid_answer = True
                        plot_medal_histogram(df_total, szn, None, games_country)
                    elif szn.lower() in ["w","winter"]: 
                        print(f"You have selected the winter olympics for {games_country}.")
                        szn = "winter"
                        valid_answer = True
                        plot_medal_histogram(df_total, szn, None, games_country)
                    else:
                        print("You have not imputted a valid season. Please start over.")
                        valid_answer = False
                else:
                    print("You have not imputted a valid country. Please input again: ")
                
            valid_req = True
            
        else:
            print("You have not imputted a valid response. Please input again: ")
             


 