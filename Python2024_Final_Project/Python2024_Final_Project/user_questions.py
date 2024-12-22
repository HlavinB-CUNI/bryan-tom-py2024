import pandas as pd
from olymp_funcs import is_valid_olympic_year

# Prompt the user to ask which olympics to start with and end with 
def ask_for_years(olymp_games):
    valid_games = False
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
            if (is_valid_olympic_year(ending_games, olymp_games) == True & (pd.to_numeric(ending_games) >= pd.to_numeric(starting_games))):
                 if szn in olymp_games['olympic_games_year'][f'{ending_games}']['seasons']:
                    print(f"There was an olympic games in {ending_games} for {szn}.")
                    valid_games = True
                    return starting_games, ending_games, szn
                 else:
                    print("You have not imputted a year of a valid olympic games. Please input again: ")
            else:
                print("You have not imputted a year of a valid olympic games. Please input again: ")
 