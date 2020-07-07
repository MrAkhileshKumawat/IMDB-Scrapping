from task13 import *


movie_list=[]
for i in range(len(scrapped1)): 
    url1=scrapped1[i]["url"]
    movies=(details_with_cast(url1))
    movie_list.append(movies)

def analyse_actors(movies_list):
    main_dic={}
    for movie in movie_list:
        for j in movie["cast"]:
            actor_id=j["imdb_id"]
            if actor_id not in main_dic:
                main_dic[actor_id]={}
                main_dic[actor_id]["name"]=j["name"]
                main_dic[actor_id]["num_movies"]=1
            else:
                main_dic[actor_id]["num_movies"]+=1
    return main_dic

# pprint.pprint(analyse_actors(movie_list))