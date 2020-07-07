import requests,pprint,os,json,time,random
from bs4 import BeautifulSoup



def scrape_top_list():
    random_sleep=random.randint(1,3)
    if os.path.exists("data/"+"task1_offline.json"):
        file=open("data/"+"task1_offline.json","r")
        file=json.load(file)
        return file
    time.sleep(random_sleep)
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    page=requests.get(url)

    soup=BeautifulSoup(page.text,"html.parser")
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.findAll("tr")

    movies_rank = []
    movies_name = []
    year_of_release = []
    movies_url = []
    movies_ratings = []

   
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=""
        for i in position:
            if "." not in i:
                rank+=i
            else:
                break
        movies_rank.append(rank)

        title = tr.find("td",class_="titleColumn").a.get_text()
        movies_name.append(title)

        year = tr.find("td",class_="titleColumn").span.get_text()
        year_of_release.append(year)

        link = tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movies_url.append(movie_link)
    
        rating = tr.find("td",class_="ratingColumn").strong.get_text()
        movies_ratings.append(rating)
    
    Top_Movies=[]
    details = {"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movies_rank)):
        details["position"]=int(movies_rank[i])
        details["name"]=str(movies_name[i])
        year_of_release[i]=year_of_release[i][1:5]
        details["year"]=int(year_of_release[i])
        details["rating"]=float(movies_ratings[i])
        details["url"]=movies_url[i]
        Top_Movies.append(details.copy())
    
    file=open("data/"+"task1_offline.json","w+")
    json.dump(Top_Movies,file)
    file.close()
    return Top_Movies


# pprint.pprint(scrape_top_list())
