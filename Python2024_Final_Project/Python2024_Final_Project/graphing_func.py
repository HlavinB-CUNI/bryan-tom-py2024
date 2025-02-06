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
        df_total.index = df_total.index.str.lower()  # Ensure indexes are lowercase
        if country not in df_total.index:
            print(f"Country '{country}' not found in the dataset.")
            return

        # Select only columns related to the chosen season
        medal_columns = df_total.filter(like=f'_total_{szn}').columns
        df_country = df_total.loc[country, medal_columns]
        
        # Extract years from column names
        years = [int(col.split('_')[0]) for col in medal_columns]
        medals = df_country.fillna(0).astype(int).values  # Replace NaN with 0 before converting


        plt.figure(figsize=(10, 5))
        plt.plot(years, medals, marker='o', linestyle='-', color='blue', label='Total Medals')

        plt.xlabel('Year')
        plt.ylabel('Total Medals')
        plt.title(f'Medals Won by {country.capitalize()} Over Time ({szn.capitalize()})')
        plt.xticks(years, rotation=45)
        plt.grid(True)
        plt.legend()
        plt.show()
        
        
