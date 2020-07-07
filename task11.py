from task5 import *

def analyse_movie_genre(movies_list):
    movie_genre={}
    for movie in movies_list:
        for genre in movie["genre"]:
            if genre not in movie_genre:
                movie_genre[genre]=1
            else:
                movie_genre[genre]+=1
    return movie_genre
    
top_movies = scrape_top_list()
movie_detail_list = get_movie_list_details(top_movies)
pprint.pprint(analyse_movie_genre(movie_detail_list))