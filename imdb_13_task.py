from urllib.request import urlopen
import json
import os.path
from pprint import pprint
import re
from bs4 import BeautifulSoup

url= "https://www.imdb.com/india/top-rated-indian-movies/"
def scrape_top_list():
    if os.path.exists("Top_movies.json"):
        with open("Top_movies.json") as file:
            print("==============================")
            read_file=file.read()
            file_store=json.loads(read_file)
        return file_store
    page=urlopen(url)
    soups=BeautifulSoup(page,"html.parser")
    main_div=soups.find("div",class_="lister")

    t_body=main_div.find("tbody",class_="lister-list")
    trs=t_body.find_all("tr")
  
    movie_ranks=[ ]
    movie_names=[ ]
    movie_Rating=[ ]
    movie_year=[ ]
    movie_url=[ ]
    movies=[ ]
    for tr in trs:
        movie_data=tr.find("td",class_="titleColumn").get_text().strip()
        rank=" "
        for data in movie_data:
            if "." not in data:
                rank=rank+data
            else:
                break
        movie_ranks.append(rank)

        movie_name=tr.find("td",class_="titleColumn").a.get_text()
        movie_names.append(movie_name)

        movie_rating=tr.find("td",class_="ratingColumn imdbRating").get_text().strip()
        movie_Rating.append(movie_rating)

        year=tr.find("td",class_="titleColumn")
        years=year.find("span",class_="secondaryInfo").get_text()
        years=(re.sub('\((\d+)\)',r'\1',years))
        movie_year.append(int(years))

        movie_link=tr.find("td",class_="titleColumn")

        movie_api=movie_link.a["href"]
        movie_li= "https://www.imdb.com/"+movie_api                                                      
        movie_url.append(movie_li)
        dis={ }
        for i in range(0,len(movie_names)):
            dis["name"] = str(movie_names[i])
            dis["year"] = movie_year[i]
            dis["position"] = int(movie_ranks[i])
            dis["rating"] =float (movie_Rating[i])
            dis["url"] = movie_url[i]
        movies.append(dis)
    # return movies
    with open("Top_movies.json","w") as file:
        print("++++++++++++++++++++++")
        json.dump(movies,file,indent=4)
    return movies                                           
scrapped = (scrape_top_list())
# print(scrapped)
def get_movie(movie_list):
    two_fifty_movie_details=[ ]
    cast_list = []
    url2 = ("fullcredits?ref_=tt_cl_sm#cast")
    for id_cast in movie_list:
        all_cast_url=(id_cast["url"]+url2)
        cast_list.append(all_cast_url)
    for cast_list_index in cast_list:
        call_nine_task=scrape_movie_details_from_imdb(cast_list_index)
        two_fifty_movie_details.append(call_nine_task)
    return two_fifty_movie_details

all_movie_details=get_movie(scrapped)
print(all_movie_details)




