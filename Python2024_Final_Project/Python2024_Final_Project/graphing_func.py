import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_countries.index, y=top_countries[f'{year}_total_{szn}'], palette='Blues')
        plt.xlabel('Country', fontsize=14, fontweight='bold')
        plt.ylabel('Total Medals', fontsize=14, fontweight='bold')
        plt.title(f'Top 10 Countries by Total Medals in {year} ({szn.capitalize()} Olympics)', fontsize=16, fontweight='bold')
        
        for index, value in enumerate(top_countries[f'{year}_total_{szn}']):
            plt.text(index, value + 0.5, str(value), ha='center', fontsize=12, fontweight='bold')
            
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
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

        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 5))
        plt.plot(years, medals, marker='o', linestyle='-', color='darkorange', linewidth=2, markersize=8, markerfacecolor='darkred')
        plt.xlabel('Year', fontsize=14, fontweight='bold')
        plt.ylabel('Total Medals', fontsize=14, fontweight='bold')
        plt.title(f'Medals Won by {country.capitalize()} Over Time ({szn.capitalize()})', fontsize=16, fontweight='bold')
    
        max_year = years[medals.argmax()]
        min_year = years[medals.argmin()]
    
        plt.annotate(f"Peak: {medals.max()} medals", xy=(max_year, medals.max()), xytext=(max_year + 1, medals.max() + 1),
                 arrowprops=dict(arrowstyle="->", lw=1), fontsize=12, fontweight='bold')
        plt.annotate(f"Valley: {medals.min()} medals", xy=(min_year, medals.min()), xytext=(min_year + 1, medals.min() - 1),
                 arrowprops=dict(arrowstyle="->", lw=1), fontsize=12, fontweight='bold')

        plt.xticks(years, rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend(['Total Medals'], loc='best', fontsize=12)
        plt.tight_layout()

        plt.show()
        
        
