from pprint import pprint
from task4 import *
from task12 import scrape_movie_cast 


def details_with_cast(movie_url):
    url=str(movie_url[27:-1])
    # return url
    
    url1="https://www.imdb.com/title/"+url+"/fullcredits?ref_=tt_cl_sm#cast"

    movie_details=scrap_movie_details(movie_url)
    cast=scrape_movie_cast(url1)
    movie_details["cast"]=cast
    return movie_details

# scrapped1=scrape_top_list()
# for i in range(len(scrapped1)): 
#     url1=scrapped1[i]["url"]
#     pprint.pprint(details_with_cast(url1))







