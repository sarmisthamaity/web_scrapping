from imdb_firsttask import*
from forth_task_imdb import*
import json
import os.path

def movie_caching(movie_url):
    movie_id=" "
    for id in movie_url[27:]:
        if "/" not in id:
            movie_id=movie_id+id
        else:
            break
    caching_name=(movie_id+".json")
    # return caching_name
    text=None
    if os.path.exists (caching_name):
        open_file=open(caching_name)
        file_read=open_file.read()
        return file_read
    movie_name_list=[ ]
    movie_director_list=[ ]
    movie_run_time=[ ]
    movie_bio_list=[ ]
    movie_genere_list=[ ]
    movie_language_list=[ ]
    movie_country_list=[ ]
    poster_url_list=[ ]

    if text is None: 
        data_get=requests.get(movie_url)
        data_get_text=data_get.text
        parser_data=BeautifulSoup(data_get_text,"html.parser")
        div_title=parser_data.find("div",class_="title_wrapper").h1.get_text()
    # return div_title
    cine_name=" "
    for d in div_title:
        if "(" not in d:
            cine_name=(cine_name+d).strip()
        else:
            break
    # return cine_name
    div_plot=parser_data.find("div",class_="plot_summary")
    div_credit=div_plot.find("div",class_="credit_summary_item")
    find_all_a=div_credit.find_all("a")
    for movie_direct in find_all_a:
        m_director=(movie_direct.get_text().strip())
        movie_director_list.append(m_director)
    # return movie_director_list
    div_text=div_plot.find("div",class_="summary_text").get_text().strip()
    # return div_text
    movie_bio_list.append(div_text)
    # return movie_bio_list
    div_sub=parser_data.find("div",class_="subtext")
    cine_time=div_sub.find("time").get_text().strip()
    # return cine_time
    convert_minute=((int(cine_time[0])*60)+(int(cine_time[3:].strip("min"))))
    # return convert_minute
    cine_genere=div_sub.find_all("a")
    # return cine_genere
    for gene in cine_genere:
        c_genere=(gene.get_text())
        movie_genere_list.append(c_genere)
    movie_genere_list.pop()
    # return movie_genere_list
    image_div=parser_data.find("div",class_="poster").img["src"]
    # return image_div
    poster_url_list.append(image_div)
    # return poster_url_list
    lang_county=parser_data.find("div",class_="article",id="titleDetails")
    all_txt_block=lang_county.find_all("div")
    for v in range(5):
        all_h4=all_txt_block[v].h4.get_text()
        # return (all_txt_block.a.get_text())
        if all_h4=="Country:":
            coun=all_txt_block[v].a.get_text()
            # return coun
            movie_country_list.append(coun)
            # return movie_country_list
        if all_h4=="Language:":
            langu=all_txt_block[v].a.get_text()
            movie_language_list.append(langu)
            # return movie_genere_list
    caching_dicts={ }
    caching_dicts["movie_name"]=cine_name
    caching_dicts["director"]=movie_director_list
    caching_dicts["genere"]=movie_genere_list
    caching_dicts["bio"]=movie_bio_list
    caching_dicts["poster_url"]=poster_url_list
    caching_dicts["country"]=movie_country_list
    caching_dicts["language"]=movie_language_list
    # return caching_dicts
    json_open=open(caching_name,"w")
    convert_json=json.dumps(caching_dicts)
    json_open.write(convert_json)
    json_open.close()
    return caching_dicts

api=("https://www.imdb.com/title/tt0093603/")
movie_data=(movie_caching(api))
# pprint.pprint(movie_data)








