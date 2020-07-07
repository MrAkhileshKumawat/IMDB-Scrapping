from task5 import *

def analyse_language_and_directors(movies_list):
    directors_name={}
    for movie in movies_list:
        for director in movie["director"]:
            if director not in directors_name:
                directors_name[director]={}
            for language in movie["language"]:
                if language not in directors_name[director]:
                    directors_name[director][language]=1
                else:
                    directors_name[director][language]+=1
    return directors_name

top_movies = scrape_top_list()
movie_detail_list = get_movie_list_details(top_movies)
pprint.pprint(analyse_language_and_directors(movie_detail_list))