# import requests
# from bs4 import BeautifulSoup
from task5 import *

def analyse_movies_language(movies_list):
    movies_language={}
    for language in movies_list:
        language=language["language"]
        for name in language:
            if name not in movies_language:
                movies_language[name]=1
            else:
                movies_language[name]+=1
    return movies_language


top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies) 
language_analysis = analyse_movies_language(movies_detail_list)
# pprint.pprint(language_analysis)