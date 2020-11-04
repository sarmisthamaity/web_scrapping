import requests
from bs4 import BeautifulSoup
import pprint
import re
url= "https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
page_text=page.text
soups=BeautifulSoup(page_text,"html.parser")

def scrape_top_list():
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
    return movies                                         
scrapped = (scrape_top_list())
# pprint.pprint(scrapped)





