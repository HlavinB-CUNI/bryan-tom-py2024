from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def bs_scrape(url_specific, location_in_series):
    # Parsing
    req = Request(
    url= url_specific, 
    headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    
    # Gathering countries and medal counts
    soup_countries_list = [tag.get_text() for tag in list(soup.find_all('span', attrs = {'data-cy':'country-name'}))]
    soup_medals_list = [tag.get_text() for tag in list(soup.find_all('span', attrs = {'data-cy':'ocs-text-module'}))]
    
    return soup_countries_list, soup_medals_list

