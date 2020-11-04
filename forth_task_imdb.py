import requests
from bs4 import BeautifulSoup
import pprint

# url=("https://www.imdb.com/title/tt0066763/")
def scrape_movie_details(movie_url):
    page=requests.get(movie_url)
    page_text=page.text
    page_soups=BeautifulSoup(page_text,"html.parser")

    name_div=page_soups.find("div",class_="title_wrapper").h1.get_text()

    movie_name=" "
    for n in name_div:
        if "(" not in n:
            movie_name=((movie_name+n).strip())
        else:
            break

    from_summry=page_soups.find("div",class_="plot_summary")
    director=from_summry.find("div",class_="credit_summary_item")
    director_name=director.find_all("a")

    names=[ ]
    for name in director_name:
        movie_director_name=(name.get_text().strip())
    
        names.append(movie_director_name)

    bio_of_movie=[ ]
    movie_bio=from_summry.find("div",class_="summary_text").get_text().strip()

    bio_of_movie.append(movie_bio)
    
    div_subtext=page_soups.find("div",class_="subtext")
    
    movie_time=div_subtext.find("time").get_text()
    str_time=(movie_time.strip().split())
    # return (len(str_time))

    if len(str_time)==2:
        for i in str_time:
            if "h" in i:
                time=int(i.strip("h"))
            if "min" in i:
                minutes=int(i.strip("min"))
        cine_time=(str(time*60+minutes)+"min")
    if len(str_time)==1:
        time=str_time[0][:-1]
        cine_time=(str(int(time)*60)+"min")
    movie_genere=div_subtext.find_all("a")
    store_genere=[ ]
    for genr in movie_genere:
        genere=(genr.get_text())
        store_genere.append(genere)
    store_genere.pop()
    
    photo=page_soups.find("div",class_="poster").img["src"]
    
    more_data=page_soups.find("div",attrs={"class":"article","id":"titleDetails"})
    data=more_data.find_all("div",class_="txt-block")
    
    lis=[ ] 
    for div in range(5):
    
        h_four=data[div].h4.get_text()

        if h_four=="Country:":
            country = data[div].a.get_text()
            
        if h_four=="Language:":
            lang =data[div].a.get_text()
            lis.append(lang)
            
    movie_details={ }
    movie_details["name"]=movie_name
    movie_details["director"]=names
    movie_details["bio"]=bio_of_movie
    movie_details["RunTime"]=cine_time
    movie_details["genere"]=store_genere
    movie_details["poster_image_url"]=photo
    movie_details["country"]=country
    movie_details["Language"]=lis

    return movie_details

url_details=scrape_movie_details(url)
# pprint.pprint(url_details)




