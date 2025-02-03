import matplotlib.pyplot as plt
import pandas as pd

def plot_medal_histogram(df_total):
    """
    Generate a histogram of total medals won by countries.
    :param df_total: DataFrame containing medal counts per country
    """

    if df_total is None or df_total.empty:
        print("No data available to plot.")
        return
    
    # Summing up all medals (gold, silver, bronze) for each country
    df_total['results'] = df_total.filter(like='2002_total_winter').sum(axis=1)
    df_total['2002_total_winter'] = pd.to_numeric(df_total['2002_total_winter'])
    
    # Sorting by total medals
    df_total_sorted = df_total.sort_values(by='2002_total_winter', ascending=False)

    # Selecting top 10 countries for better visualization
    top_countries = df_total_sorted.head(10)
    print(df_total)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.bar(top_countries.index, top_countries['2002_total_winter'], color='gold')
    plt.xlabel('Country')
    plt.ylabel('results')
    plt.title('Top 10 Countries by Total Medals')
    plt.xticks(rotation=45)
    plt.show()
