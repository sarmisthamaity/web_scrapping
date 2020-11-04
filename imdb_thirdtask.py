from imdb_sectask import*
import numpy as np
# pprint.pprint (movies_by_year)
def group_by_decade(movie):
    # return movies
    dic_ten=0
    lis=[ ]
    decade=[ ]
    decade_dic={ }
    for u in movie:
        lis.append(u)
    # return lis
    lis.sort()
    # return lis
    for y in (lis): 
        deca=int(np.floor(y/10)*10)
        decade.append(deca)
        decades=set(decade)
    # return decades
    convert_list=list(decades)
    # return (type(convert_list))
    convert_list.sort()
    # return convert_list
    for c in convert_list:
        # return c
        dec_ten=c+9
        data=[ ]
        for m in movie:
            # return m
            if m<=dec_ten and m>=c:
                # return m
                for z in movie[m]:
                    # return z
                    if z not in data:
                        data.append(z)
        decade_dic[c]=data
    return decade_dic
pprint.pprint(group_by_decade(movies_by_year))




# 