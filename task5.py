import requests
from bs4 import BeautifulSoup
from task4 import *

def get_movie_list_details(movie_list):
    movie_detail_list = []
    for i in movie_list:
        details= scrap_movie_details(i["url"])
        movie_detail_list.append(details)
        
    return movie_detail_list

top_movies = scrape_top_list()
movie_detail_list = get_movie_list_details(top_movies[:10])
# pprint.pprint(movie_detail_list)