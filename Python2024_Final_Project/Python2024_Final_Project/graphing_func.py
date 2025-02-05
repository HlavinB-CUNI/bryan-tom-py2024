import matplotlib.pyplot as plt
import pandas as pd

def plot_medal_histogram(df_total, szn, year, country):
    """
    Generate a histogram of total medals won by countries. Or medals won by a specific country over time. 
    :param df_total: DataFrame containing medal counts per country
    """

    if df_total is None or df_total.empty:
        print("No data available to plot.")
        return
    
    # Graphing for Top 10 Medals for a Specific Olympics
    if country == None:
        # Summing up all medals (gold, silver, bronze) for each country
        df_total['results'] = df_total.filter(like=f'{year}_total_{szn}').sum(axis=1)
        df_total[f'{year}_total_{szn}'] = pd.to_numeric(df_total[f'{year}_total_{szn}'])
    
        # Sorting by total medals
        df_total_sorted = df_total.sort_values(by=f'{year}_total_{szn}', ascending=False)

        # Selecting top 10 countries for better visualization
        top_countries = df_total_sorted.head(10)

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.bar(top_countries.index, top_countries[f'{year}_total_{szn}'], color='gold')
        plt.xlabel('Country')
        plt.ylabel('results')
        plt.title('Top 10 Countries by Total Medals')
        plt.xticks(rotation=45)
        plt.show()
        
    # Graphing for a Country's Medals Over Time
    else:
        country = country.lower()
        df_lowercase = df_total.copy()
        df_lowercase.index = df_lowercase.index.str.lower()
        print(df_lowercase.loc[f'{country}'])
        
        # GRPAHING GOES HERE
