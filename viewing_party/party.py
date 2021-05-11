def create_movie(title, genre, rating):
    # print("********************")
    if title and genre and rating:
        return {
        "title" : title,
        "genre" : genre,
        "rating" : rating

    }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched" : [movie]
    }
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist" : [movie]
    }
    return user_data

def watch_movie(user_data, title):
    # user_data = {
    #     "watchlist" : [],
    #     "watched": []
    # }
    i = 0
    watchlist = user_data["watchlist"]

    for i in range (len(watchlist)):
        if watchlist[i]["title"] == title:
            user_data["watched"].append(watchlist[i])
            watchlist.pop(i)
            return user_data
            break
    return user_data

def get_watched_avg_rating(user_data):
    ratings = []
    ratings_sum = 0

    if len(user_data["watched"]) == 0:
            return 0.0
    
    i = 0
    for i in range (len(user_data["watched"])):
        ratings.append(user_data["watched"][i]["rating"])
        ratings_sum += user_data["watched"][i]["rating"]
    
    avg_rating = ratings_sum / len(ratings)

    return avg_rating

def get_most_watched_genre(user_data):
    genre_count = {}

    if len(user_data["watched"]) == 0:
        return None

    for item in user_data["watched"]:
        if (item["genre"] in genre_count):
            genre_count[item["genre"]] += 1
        else:
            genre_count[item["genre"]] = 1
    
    most_frequent_genre = max(genre_count, key=genre_count.get)

    return most_frequent_genre

def get_unique_watched(user_data):
    unique_watched = []
    friends = user_data["friends"]
    friends_watched_list = []
    i = 0
    
    for i in range(len(friends)):
        friends_watched = friends[i]["watched"]
        for i in range(len(friends_watched)):
            if friends_watched[i] not in friends_watched_list:
                friends_watched_list.append(friends_watched[i])
    
    for item in user_data["watched"]:
        if item not in friends_watched_list:
            unique_watched.append({"title" : item["title"]})

    return unique_watched

    
def get_friends_unique_watched(user_data):
    unique_unwatched = []
    user = user_data["watched"]
    friends = user_data["friends"]
    user_watched = []
    i = 0
    
    for i in range(len(user)):
        if user[i] not in user_watched:
            user_watched.append(user[i])
    
    for i in range(len(friends)):
        friends_watched = friends[i]["watched"]
        for i in range(len(friends_watched)):
            if (friends_watched[i] not in user_watched) and (friends_watched[i] not in unique_unwatched):
                unique_unwatched.append(friends_watched[i])

    return unique_unwatched

def get_available_recs(user_data):
    recommended_movies = []
    user_subscriptions = user_data["subscriptions"]
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    i = 0

    for i in range(len(friends)):
        friends_watched = user_data["friends"][i]["watched"]
        for i in range(len(friends[i]["watched"])):
            
            if (friends_watched[i]["title"] not in user_watched) and (friends_watched[i]["host"] in user_subscriptions):
                if friends_watched[i] not in recommended_movies:
                    recommended_movies.append(friends_watched[i])

    return recommended_movies

def get_new_rec_by_genre(user_data):
    genre_count = {}
    recommended_movies = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    

    if len(user_data["watched"]) == 0:
        return recommended_movies

    for item in user_data["watched"]:
        if (item["genre"] in genre_count):
            genre_count[item["genre"]] += 1
        else:
            genre_count[item["genre"]] = 1
    
    most_frequent_genre = max(genre_count, key=genre_count.get)

    for i in range(len(friends)):
        friends_watched = user_data["friends"][i]["watched"]
        for i in range(len(friends[i]["watched"])):   
            if (friends_watched[i]["title"] not in user_watched) and (friends_watched[i]["genre"] == most_frequent_genre):
                if friends_watched[i] not in recommended_movies:
                    recommended_movies.append(friends_watched[i])

    

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    friends_watched_list = []
    favorites = user_data["favorites"]
    friends = user_data["friends"]

    for i in range(len(friends)):
        friends_watched = user_data["friends"][i]["watched"]
        for i in range(len(friends_watched)):
            if friends_watched[i] not in friends_watched_list:
                    friends_watched_list.append(friends_watched[i])

    for i in range(len(favorites)):
        if favorites[i] not in friends_watched_list:
            recommended_movies.append(favorites[i])

    return recommended_movies