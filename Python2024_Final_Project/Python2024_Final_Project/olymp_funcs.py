import datetime
import time
import random
import requests
import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

       
def is_valid_olympic_year(year, games_json):
    if (year in games_json['olympic_games_year'].keys()):
        return True
    else:
        return False    
    

        