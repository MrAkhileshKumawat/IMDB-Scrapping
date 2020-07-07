from task4 import *

def scrape_movie_cast(movie_cast_url):
    id=movie_cast_url[27:36]

    if os.path.exists("data/cast_details/"+id+"_cast.json"):
        file=open("data/cast_details/"+id+"_cast.json","r")
        data=json.load(file)
        file.close()
        return data
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    table_data=soup.find("table" , class_="cast_list")
    actors=table_data.findAll("td",class_="")
    castlist=[]
    for actor in actors:
        actors_dict={}
        imdb_id=actor.find("a").get("href")[6:15]
        actor_name=actor.getText().strip()
        actors_dict["imdb_id"]=str(imdb_id)
        actors_dict["name"]=str(actor_name)
        castlist.append(actors_dict)
    
    ## CACHING
    file=open("data/cast_details/"+id+"_cast.json","w")
    json.dump(castlist,file)
    file.close()
    return castlist
    

# for i in id_list:
#     print(i)   
#     url="https://www.imdb.com/title/"+str(i)+"/fullcredits?ref_=tt_cl_sm#cast"
#     pprint.pprint(scrape_movie_cast(url))
