from fifth_part2_webscrappping import*
# from nine_task_imdb import*

def analyse_language_and_directors(movie_details):
    all_directors={ }
    for d in (movie_details):

        for director in d["director"]:
            all_directors["name"]=director
            all_directors[director]={ }
    
    for di in range(len(movie_details)):
        for director in all_directors:
            if director in movie_details[di]["director"]:
                for lang in movie_details[di]["Language"]:
                    all_directors[director][lang]=0
    
    for j in range(len(movie_details)):
        for director in all_directors:
            if director in movie_details[j]["director"]:   
                for lang in movie_details[j]["Language"]:
                    all_directors[director][lang]+=1 

    return all_directors

all_movie=analyse_language_and_directors(ten_movie_details)
# print(all_movie)
