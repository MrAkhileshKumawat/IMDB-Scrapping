import requests,pprint,os,json,random,time
from bs4 import BeautifulSoup
from task1 import *

id_list=[]
def scrap_movie_details(movie_url):
    # TASK 8
    url=str(movie_url[27:-1])
    id_list.append(url)
    if os.path.exists("data/movie_details/"+url+".json"):
        file=open("data/movie_details/"+url+".json","r")
        data=json.load(file)
        file.close()
        return data


    # Task 9
    random_range=random.randint[1,3]
    time.sleep(random_range)
    

    # TASK 4
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')
    movieDetail={}
	# here i find movie name
    name_div=soup.find("div",class_="title_wrapper").h1.text
    movie_name=""
    for i in name_div:
        if i in "(":
            break
        else:
            movie_name+=i.strip()
        # return movie_name

    # In this div we get all other things like gener,runtime and many more
    sub_div=soup.find("div",class_="subtext")

    # here I scrape movie runtime
    runtime=sub_div.find("time").get_text().strip().split()
    minutes = 0
    for Time in runtime:
        if 'h' in Time:
            hours_to_min = int(Time.strip('h')) * 60
        elif 'min' in Time:
            minutes = int(Time.strip('min'))
    movie_runtime = hours_to_min + minutes
    # return runtime

    # here i scrap movie gener
    geners=sub_div.find_all("a")
    geners.pop()
    movie_gener=[gener.get_text() for gener in geners]
    # return movie_gener

    #her i find director name and bio
    summary=soup.find("div",class_="plot_summary")
    
    # here I scrap Movie_bio
    movie_bio=summary.find("div",class_="summary_text").get_text().strip()
    # return movie_bio

    # here I scrap Movie_director
    director_div=summary.find("div",class_="credit_summary_item")
    director_name=director_div.find_all("a")
    movie_director=[director.get_text().strip() for director in director_name]
    # return movie_director

    # In this div we get country and language
    country_lang_div = soup.find("div",attrs={"class":"article","id":"titleDetails"})
    list_of_dives = country_lang_div.findAll("div")
    for check_div in list_of_dives:
        detail_list = check_div.get_text().split()
        if detail_list[0] == "Country:":
            movie_country = check_div.find('a').get_text()
        elif detail_list[0] =="Language:":
            a_tag_list = check_div.find_all('a')
            movie_language = [language.get_text() for language in a_tag_list]            
    # return movie_language

    # Here I scrap Poster Image_url.
    movie_poster_link=soup.find("div",class_="poster").a["href"]
    movie_poster="https://www.imdb.com"+movie_poster_link
    # return movie_poster
    
    # Here I create Dic for movie-details
    movie_detail_dic={"name":"","director":"","bio":"","runtime":"","genre":"","country":"","language":"","poster_image_url":""}

    movie_detail_dic["name"]=movie_name
    movie_detail_dic["director"]=movie_director
    movie_detail_dic["bio"]=movie_bio
    movie_detail_dic["runtime"]=movie_runtime
    movie_detail_dic["genre"]=movie_gener
    movie_detail_dic["country"]=movie_country
    movie_detail_dic["language"]=movie_language
    movie_detail_dic["poster_image_url"]=movie_poster

    # Task 8
    file=open("data/movie_details/"+url+".json","w")
    json.dump(movie_detail_dic,file)
    file.close()
    
    return movie_detail_dic

scrapped1=scrape_top_list()
for i in range(len(scrapped1)): 
    url1=scrapped1[i]["url"]
    movie_detail=scrap_movie_details(url1)
    # pprint.pprint(movie_detail)