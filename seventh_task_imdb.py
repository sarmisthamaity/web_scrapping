from imdb_firsttask import*
from forth_task_imdb import*
from fifth_part2_webscrappping import*

def analyse_movies_directors(movie_list):
    # return movie_list
    director=[ ]
    count_director=[ ]
    director_dicts={ }
    for d_name in movie_list:
        for d_name in d_name["director"]:
            director.append(d_name)
    # return director
    for n in director:
        if n not in count_director:
            count_director.append(n)
    # return count_director
    
    for d_name in director:
        count=0
        for n in count_director:
            if d_name==n:
                count=count+1
            director_dicts[d_name]=count
    return director_dicts

analyse_director=(analyse_movies_directors(ten_movie_details))
pprint.pprint(analyse_director)




