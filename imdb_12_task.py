from bs4 import BeautifulSoup
from pprint import pprint
from urllib.request import urlopen


caste_url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
def movie_caste_url(url):
    page=urlopen(url)
    page_parser=BeautifulSoup(page,"html.parser")
    # print(page_parser)
    find_div=page_parser.find("div",id="fullcredits_content",class_="header")
    # print(find_div)
    find_table=find_div.find("table",class_="cast_list")
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

id_name=movie_caste_url(caste_url)
print(id_name)


