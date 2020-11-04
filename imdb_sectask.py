
from imdb_firsttask import *
# pprint.pprint(scrapped)

def group_by_year(movies):
    # return movies
    year_release=[ ]
    dists={ }
    for year in range(len(movies)):
        movie_year=(movies[year]["year"])
        if movie_year not in year_release:
            year_release.append(movie_year)
    # return year_release
    for y in (year_release):
        yers=[ ]
        for r in range(len(movies)):
            if y== movies[r]["year"]:
                yers.append(movies[r])

        dists[y]=yers
    return dists     
movies_by_year=group_by_year(scrapped)
# pprint.pprint(movies_by_year)

