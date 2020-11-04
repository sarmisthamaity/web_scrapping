
from fifth_part2_webscrappping import*

def analyse_movies_genre(movie_list):
    
    genere_dicts={ }
    for g in movie_list:
        lis_genere=g["genere"]
        for gener_index in lis_genere:
            if gener_index in genere_dicts:
                genere_dicts[gener_index]+=1
            else:
                genere_dicts[gener_index]=1
    return genere_dicts

all_genere=analyse_movies_genre(ten_movie_details)
pprint.pprint(all_genere)

