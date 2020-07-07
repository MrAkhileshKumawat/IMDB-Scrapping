# import requests
# from bs4 import BeautifulSoup
from task5 import *


def analyse_movies_directors(movies_list):
    movies_director={}
    for director in movies_list:
        director=director["director"]
        for name in director:
            if name not in movies_director:
                movies_director[name]=1
            else:
                movies_director[name]+=1
    return movies_director

top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies)
director_analysis = analyse_movies_directors(movies_detail_list)
# pprint.pprint(director_analysis)