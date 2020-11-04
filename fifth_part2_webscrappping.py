from imdb_firsttask import *
from forth_task_imdb import *
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




