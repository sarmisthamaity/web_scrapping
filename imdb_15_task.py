from urllib.request import urlopen
import json
import os.path
from bs4 import BeautifulSoup
import pprint
import re


#### Task 1
url= "https://www.imdb.com/india/top-rated-indian-movies/"
def scrape_top_list():
    if os.path.exists("Top_movies.json"):
        with open("Top_movies.json") as file:
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
    with open("Top_movies.json","w") as file:
        json.dump(movies,file,indent=4)

    return movies                                         
scrapped = (scrape_top_list())
# print(scrapped)


###Task 12
# caste_url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"

def movie_caste_url(url):

    page=urlopen(url)
    
    page_parser=BeautifulSoup(page,"html.parser")
    # print(page_parser)
    # find_div=page_parser.find("div",id="fullcredits_content",class_="header")
    # print(find_div)
    find_table=page_parser.find("table",class_="cast_list")
    # print(find_table)
    find_td=find_table.find_all("td",class_="")
    # print(find_td)    
    name_list=[ ]
    id_list=[ ]
    store_list=[ ]
    for t in find_td:
        name=(t.get_text()).strip()
        name_list.append(name)
        ids=t.find("a")["href"][6:15]
        id_list.append(ids)
    for dics_index in range(len(id_list)):
        ids_dics={ }
        ids_dics["Name"]=name_list[dics_index]
        ids_dics["ID"]=id_list[dics_index]
        store_list.append(ids_dics)
    return store_list

# id_name=movie_caste_url(caste_url)
# print(id_name)

#### 4 Task

def scrape_movie_details(movie_url):
    id_name=movie_caste_url(movie_url)
    page=urlopen(movie_url)
    page_soups=BeautifulSoup(page,"html.parser")

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
    movie_language_list=[ ]
    movie_country_list=[ ]
    count=0
    for txt_block_indx in data:
        txt_all_h4=txt_block_indx.find("h4",class_="inline")
        if count==2:    
            break
        if txt_all_h4.get_text()=="Country:":
            coun=txt_block_indx.find("a").get_text()
            movie_country_list.append(coun)
            count=count+1
        if txt_all_h4.get_text()=="Language:":
            langu=txt_block_indx.find_all("a")
            for la in langu:
                movie_language_list.append(la.get_text())
            count=count+1
            
    movie_details={ }
    movie_details["name"]=movie_name
    movie_details["director"]=names
    movie_details["bio"]=bio_of_movie
    movie_details["RunTime"]=cine_time
    movie_details["genere"]=store_genere
    movie_details["poster_image_url"]=photo
    movie_details["country"]=movie_country_list
    movie_details["Language"]=movie_language_list
    movie_details["Cast"]=id_name
    return movie_details

url_details=scrape_movie_details(url)
# pprint.pprint(url_details)

###task 5

api_list=[ ]
def get_movie_list_details(movie_list):
    top_movie_details=[ ]
    for api in movie_list[:30]:
        api_list.append(api["url"])
    # return api_list
    for api_list_index in api_list:
        url_data=scrape_movie_details(api_list_index)
        top_movie_details.append(url_data)
    return top_movie_details

ten_movie_details=get_movie_list_details(scrapped)   
# pprint.pprint(ten_movie_details) 

########## 15 task

def analyse_actors(movies):
    newDic = {}
    for i in range(len(movies)):     
        count = 1
        for j in movies[i]['Cast']:        
            one = j['ID']
            for i2 in range(i+1 ,len(movies)):      
                for j2 in movies[i2]['Cast']:  
                    two = j2['ID']
                    if(one == two):
                        count+=1        
                        newDic[j['ID']] = ({'Name' : j['Name'], 'num_movies' : count})
    return newDic

print(analyse_actors(ten_movie_details))



