def create_movie(movie_title, genre, rating):
    movie={}
    if movie_title == None or genre == None or rating ==None :
        return None
    else :
        movie["title"]=movie_title
        movie["genre"]=genre
        movie["rating"]=rating
    return movie
        

def add_to_watched(user_data, movie):
    # print(user_data,user_data["watched"])
    if len(user_data["watched"]) == 0:
    
        user_data["watched"]=[movie]
    elif len(user_data["watched"]) == 1:
        return 1
    return user_data
    

def add_to_watchlist(user_data, movie):
    if len(user_data["watchlist"]) == 0:
        user_data["watchlist"]=[movie]
    elif len(user_data["watchlist"]) == 1:
        return 1
    return user_data



# def watch_movie(janes_data, name):
#     for key,value in janes_data.items():
#         print("data",key, value)
#         if key == "watchlist":
#             for names in value:
#                 print("name", names)
#                 if name == names["title"]:
#                     print("yes",names)
#                     janes_data["watched"].append(names)
#                     janes_data["watchlist"].pop()
#     return janes_data


def watch_movie(janes_data, name):

    for key,value in janes_data.items():
        print("data",key, value)
        if key == "watchlist":
            for names in value:
                index=0
                print("name", names)
                if name == names["title"]:
                    print("yes")
                    janes_data["watched"].append(names)
                    del janes_data["watchlist"][index]
                    print("jj",janes_data)
                index+=1
    return janes_data