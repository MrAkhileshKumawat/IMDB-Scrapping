# import requests,pprint
# from bs4 import BeautifulSoup
from task2 import *


def group_by_decode(movies):
    movies_by_year=group_by_year(movies)
    moviesdec={}
    year=[]
    for i in movies_by_year:
        mod=i%10
        decade=i-mod
        if decade not in year:
            year.append(decade)
    # return year
    year.sort()
    for i in year:
        moviesdec[i]=[]
    for i in moviesdec:
            dec10=i+9
            for x in movies_by_year:
                if x<=dec10 and x>=i:
                    for v in movies_by_year[x]:
                        moviesdec[i].append(v)
    return moviesdec


decode_year=group_by_decode(scrapped1)
# pprint.pprint(decode_year)