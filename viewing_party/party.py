# test_wave_01
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



# test_wave_02
def get_watched_avg_rating(janes_data):
    result=0
    index=0
    if len(janes_data["watched"]) == 0:
       return 0.0

    for key, values in janes_data.items():
        for movie_title in values:
            if len(values) != 0:
               result+=values[index]["rating"]
               index+=1
            else:
               return 0.0
    return result/len(janes_data["watched"])



def get_most_watched_genre(janes_data):
    max_genre={}
    
    for values in janes_data.values():
        if len(values) == 0:
            return None
        for movie_name in values:
          
            if movie_name["genre"] not in max_genre:
               
               max_genre[movie_name["genre"]]=1
               
            else:
           
              max_genre[movie_name["genre"]]+=1
              

           
    max_num=max_genre.values()
    max_num=max(max_num)


    for key, value in max_genre.items():
        if value == max_num:
            return key


# test_wave_03

def get_unique_watched(amandas_data):
    friends_watched_list=[]
    result=[]
    for friend in amandas_data["friends"]:
        for movie in friend["watched"]:
             friends_watched_list.append(movie["title"])
             print("ss",movie["title"])
                   
    for watched_list in amandas_data["watched"]:
        for key_val,vals in watched_list.items():
            if vals not in friends_watched_list:
                print("ddd",vals)
                result.append(watched_list)
    return result


def get_friends_unique_watched(amandas_data):
    user_watched_list=[]
    result=[]
    for watched in amandas_data["watched"]:
        print(watched)
      
        user_watched_list.append(watched)
    for friends_watched in amandas_data["friends"]:
        for watched, watched_list in friends_watched.items():
            print("ss",watched_list)
            for val in watched_list:
                print("aas",val)
                if val not in user_watched_list:
                    result.append(val)
    return [dict(t) for t in {tuple(d.items()) for d in result}]


# test_wave_04


def get_available_recs(amandas_data):
    print("hh",amandas_data["watched"])
    empty_user_watched_list=True
    friend_watched_list=[]
    
    result=[]
    for watched in amandas_data["friends"]:
      
        for key_val,val_list in watched.items():
       
            for val in val_list:
               
                friend_watched_list.append(val)
    print(friend_watched_list)

    while empty_user_watched_list:
        for item in friend_watched_list:
            
            if item["host"] in amandas_data["subscriptions"]:
                result.append(item)
        
        empty_user_watched_list=False

    return [dict(t) for t in {tuple(d.items()) for d in result}]


# test_wave_05
def get_new_rec_by_genre(sonyas_data):
    genre=[]
    user_watched=[]
    result=[]
    for user_movie in sonyas_data["watched"]:
            if user_movie["genre"] not in genre:
               genre.append(user_movie["genre"])
            user_watched.append(user_movie["title"])
            print("dd",genre,user_watched)
    
    for friends_movie in sonyas_data["friends"]:
        for movie in friends_movie["watched"]:
           if movie["title"] not in user_watched and movie["genre"] in genre:
              print("hhh")
              result.append(movie)
    print("fff",result)
    return result



def get_rec_from_favorites(sonyas_data):
    user_favorite_list=[]
    friends=sonyas_data["friends"][0]["watched"]+sonyas_data["friends"][1] ["watched"]
    result=[]
    for favorites_movie in sonyas_data["favorites"]:
        if favorites_movie in sonyas_data["watched"]:
           user_favorite_list.append(favorites_movie)
        print(user_favorite_list)

  
    for favorite in user_favorite_list:
            if favorite not in friends:
               result.append(favorite)
             

    return result