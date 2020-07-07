import requests
import pprint
from bs4 import BeautifulSoup
from task1 import *


def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict = {i:[] for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if x==year:
                movie_dict[x].append(i)
    return movie_dict

scrapped1=scrape_top_list()
# pprint.pprint(group_by_year(scrapped1))   