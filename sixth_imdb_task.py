from imdb_firsttask import*
from forth_task_imdb import*
from fifth_part2_webscrappping import*

def analyse_movies_language(movie_list):
    cine_language=[ ]
    langu=[]
    data_store={ }
    for lan in movie_list:
        for l in lan["Language"]:
            cine_language.append(l)
    # return cine_language
    for la in cine_language:
        if la not in langu:
            langu.append(la)
    # return langu
    for i in langu:
        count=0
        for j in cine_language:
            if j==i:
                count=count+1
            data_store[i]=count

    return data_store

ten_movie_count=(analyse_movies_language(ten_movie_details))
# pprint.pprint(ten_movie_count)

