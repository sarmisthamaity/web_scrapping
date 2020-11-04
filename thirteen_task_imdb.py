from urllib.request import urlopen
import json
import random,time
import os.path
from bs4 import BeautifulSoup
import re

url= "https://www.imdb.com/india/top-rated-indian-movies/"
def scrape_top_list():
    if os.path.exists("Top_250_movies.json"):
        with open("Top_250_movies.json") as file:
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
    with open("Top_250_movies.json","w") as file:
        print("++++++++++++++++++++++")
        json.dump(movies,file,indent=4)
    return movies                                       
scrapped = (scrape_top_list())
# print(scrapped)

##### task_12###########
def movie_caste_url(url):
    page=urlopen(url)
    page_parser=BeautifulSoup(page,"html.parser")
    find_table=page_parser.find("table",class_="cast_list")
    find_td=find_table.find_all("td",class_="")

    name_list=[ ]
    id_list=[ ]
    store_list=[ ]
    for t in find_td:
        name=(t.get_text()).strip()
        name_list.append(name)
        ids=t.find("a")["href"][6:15]
        id_list.append(ids)
    for dics_index in range(len(id_list)):
        caching_dicts={ }
        caching_dicts["Name"]=name_list[dics_index]
        caching_dicts["ID"]=id_list[dics_index]
        store_list.append(caching_dicts)
    return store_list
    
# cast=movie_caste_url(scrapped)
# print(cast)

# # ## nine_task##

def scrape_movie_details_from_imdb(movie_url):
    sleep=random.randint(1,3)
    time.sleep(sleep)
    title_caching_name=""
    for title_id_index in movie_url[28:]:
        if "/" in title_id_index:
            break
        else:
            title_caching_name=title_caching_name+title_id_index
    fifty_movie_name=(title_caching_name+".json")
    movie_director_list=[ ]
    movie_run_time=[ ]
    movie_bio_list=[ ]
    movie_genere_list=[ ]
    movie_language_list=[ ]
    movie_country_list=[ ]
    poster_url_list=[ ]

    text=None
    if os.path.exists(fifty_movie_name):
        with open (fifty_movie_name,"r") as all_caching_file:
            caching_read=all_caching_file.read()
            return (caching_read)
    if text is None:
        all_get=urlopen(movie_url)
        # all_get_text=all_get.text
        all_text_parser=BeautifulSoup(all_get,"html.parser")
        div_title=all_text_parser.find("div",class_="title_wrapper").h1.get_text()
    cine_name=""
    for d in div_title:
        if "(" in d:
            break
        else:
            cine_name=(cine_name+d).strip()

    div_plot=all_text_parser.find("div",class_="plot_summary")
    div_credit=div_plot.find("div",class_="credit_summary_item")
    find_all_a=div_credit.find_all("a")
    for movie_direct in find_all_a:
        m_director=(movie_direct.get_text().strip())
        movie_director_list.append(m_director)

    div_text=div_plot.find("div",class_="summary_text").get_text().strip()

    movie_bio_list.append(div_text)

    div_sub=all_text_parser.find("div",class_="subtext")
    cine_time=div_sub.find("time").get_text().strip().split()
    # return cine_time
    if len(cine_time)==2:
        for t in cine_time:
            if "h" in t:
                tim=int(t.strip("h"))
            if "min" in t:
                minutes=int(t.strip("min"))
        runtime=(str(tim*60+minutes)+"min")
    if len(cine_time)==1:
        ti=cine_time[0][:-1]
        runtime=(str(int(ti)*60)+"min")
    cine_genere=div_sub.find_all("a")

    for gene in cine_genere:
        c_genere=(gene.get_text())
        movie_genere_list.append(c_genere)
    movie_genere_list.pop()

    image_div=all_text_parser.find("div",class_="poster").img["src"]

    poster_url_list.append(image_div)

    lang_county=all_text_parser.find("div",class_="article",id="titleDetails")
    all_txt_block=lang_county.find_all("div",class_="txt-block")
    count=0
    for txt_block_indx in all_txt_block:
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
    caching_dicts={ }
    caching_dicts["movie_name"]=cine_name
    caching_dicts["director"]=movie_director_list
    caching_dicts["genere"]=movie_genere_list
    caching_dicts["bio"]=movie_bio_list
    caching_dicts["poster_url"]=poster_url_list
    caching_dicts["country"]=movie_country_list
    caching_dicts["Language"]=movie_language_list
    caching_dicts["RunTime"]=runtime
    caching_dicts["Cast"]=store_list
    with open(fifty_movie_name,"w") as fifty_file:                       
        convert_dump=json.dumps(caching_dicts,indent=4)
        json_write=fifty_file.write(convert_dump)
        fifty_file.close()
    return caching_dicts    

def get_movie(movie_list):
    two_fifty_movie_details=[ ]
    cast_list = []
    all_url_list=[ ]
    url2 = ("fullcredits?ref_=tt_cl_sm#cast")
    for id_cast in movie_list:
        all_cast_url=(id_cast["url"]+url2)
        cast_list.append(all_cast_url)
    for ur in movie_list:
        all_url=ur["url"]
        all_url_list.append(all_url)
    for all_url_list_index in all_url_list:
        call_nine_task=scrape_movie_details_from_imdb(all_url_list_index)
        two_fifty_movie_details.append(call_nine_task)
    return two_fifty_movie_details

all_movie_details=get_movie(scrapped)
print(all_movie_details)


