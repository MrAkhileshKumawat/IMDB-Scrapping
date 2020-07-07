# import requests
# from bs4 import BeautifulSoup
from task4 import *
import os,json

def save_scrap_movie_details(movie_url,movie_detail):
    movie_id=""
    for id in movie_url[27:]:
        if "/" not in id:
            movie_id+=id
        else:
            break
    file_name=movie_id+".json"
    # return file_name

    if os.path.exists("data/movie_details/"+file_name):
        file1=open("data/movie_details/"+file_name,"r")
        file1=json.load(file1)
        return file1
    else:
        file1=open("data/movie_details/"+file_name,"w+")
        raw = json.dumps(movie_detail)
        file1.write(raw)
        file1.close()
        return movie_detail

scrapped1=scrape_top_list()
for i in range(len(scrapped1)):
    url1=scrapped1[i]["url"]
    movie_detail=scrap_movie_details(url1)
    pprint.pprint(save_scrap_movie_details(url1,movie_detail))