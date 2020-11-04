import random
import time
from imdb_firsttask import*
import json
import os.path
from pprint import pprint

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

    movie_name_list=[ ]
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
        all_get=requests.get(movie_url)
        all_get_text=all_get.text
        all_text_parser=BeautifulSoup(all_get_text,"html.parser")
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
    all_txt_block=lang_county.find_all("div")
    for v in range(5):
        all_h4=all_txt_block[v].h4.get_text()
        
        if all_h4=="Country:":
            coun=all_txt_block[v].a.get_text()

            movie_country_list.append(coun)

        if all_h4=="Language:":
            langu=all_txt_block[v].a.get_text()
            movie_language_list.append(langu)

    caching_dicts={ }
    caching_dicts["movie_name"]=cine_name
    caching_dicts["director"]=movie_director_list
    caching_dicts["genere"]=movie_genere_list
    caching_dicts["bio"]=movie_bio_list
    caching_dicts["poster_url"]=poster_url_list
    caching_dicts["country"]=movie_country_list
    caching_dicts["language"]=movie_language_list
    caching_dicts["RunTime"]=runtime

    with open(fifty_movie_name,"w") as fifty_file:                       
        convert_dump=json.dumps(caching_dicts,indent=4)
        json_write=fifty_file.write(convert_dump)
        fifty_file.close()
    return caching_dicts    

def get_movie(movie_list):

    two_fifty_movie_details=[ ]
    two_fifty_movie_url=[ ]
    for api in movie_list[0:100]:
        two_fifty_movie_url.append(api["url"])

    for movie_url_index in two_fifty_movie_url:
        call_forth_task=scrape_movie_details_from_imdb(movie_url_index)
        two_fifty_movie_details.append(call_forth_task)
    return two_fifty_movie_details
all_movie_details=get_movie(scrapped)
# print(all_movie_details)


