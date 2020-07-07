from task13 import *


movie_list=[]
for i in range(5): 
    url1=scrapped1[i]["url"]
    movies=(details_with_cast(url1))
    movie_list.append(movies)
# pprint.pprint(movie_list)

def analyse_co_actors(movies_list):
    co_actors={}
    for i in movies_list:
        actor_id=i["cast"][0]["imdb_id"]
        if actor_id not in co_actors:
            co_actors[actor_id]={}
            co_actors[actor_id]["name"]=i["cast"][0]["name"]
            co_actors[actor_id]["frequently_co_actors"]=[]
        for j in i["cast"][1:6]:
            for k in co_actors[actor_id]["frequently_co_actors"]:
                if k["imdb_id"]==j["imdb_id"]:
                    k["num_movies"]+=1
                else:
                    freq_co_dict={}
                    freq_co_dict["imdb_id"]=j["imdb_id"]
                    freq_co_dict["name"]=j["name"]
                    freq_co_dict["num_movies"]=1
                    co_actors[actor_id]["frequently_co_actors"].append(freq_co_dict)
            else:
                freq_co_dict={}
                freq_co_dict["imdb_id"]=j["imdb_id"]
                freq_co_dict["name"]=j["name"]
                freq_co_dict["num_movies"]=1
                co_actors[actor_id]["frequently_co_actors"].append(freq_co_dict)
    return co_actors

# pprint.pprint(analyse_co_actors(movie_list))

