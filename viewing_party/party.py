def create_movie(movie_title, genre, rating):
    new_movie = {}

    if movie_title == None or genre == None or rating == None:
        return None
    else:
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, movie):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]

    return user_data

def get_watched_avg_rating(user_data):
    rating_sum = 0

    if len(user_data["watched"]) < 1:
        return 0

    for movie_item in user_data["watched"]:
        rating_sum += movie_item["rating"]

    return rating_sum/len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched = None
    watched_cnt = 0

    for movie_item in user_data["watched"]:
        if movie_item["genre"] in genre_count:
            genre_count[movie_item["genre"]] += 1
        else:
            genre_count[movie_item["genre"]] = 1

    for genre in genre_count.items():
        if genre[1] > watched_cnt:
            watched_cnt = genre[1]
            most_watched = genre[0]

    return most_watched

def get_unique_watched(user_data):
    user_watched = user_data["watched"].copy()
    friends_watched = []
    user_unique_watched = []

    for watched_list in user_data["friends"]:
        for movie_item in watched_list["watched"]:
            friends_watched.append(movie_item["title"])

    for movie_item in user_watched:
        if movie_item["title"] not in friends_watched:
            user_unique_watched.append(movie_item)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = []
    friends_unique_watched = []

    for watched_list in user_data["friends"]:
        for movie_item in watched_list["watched"]:
            print("movie item******", movie_item)
            print("movie_item not in friends_watched", movie_item not in friends_watched)
            if movie_item not in friends_watched:
                friends_watched.append(movie_item)

    for i in range(len(friends_watched)):
        if friends_watched[i] not in user_watched:
            friends_unique_watched.append(friends_watched[i])

    return friends_unique_watched

def get_available_recs(user_data):
    friends_watched = []
    recommendations = []

    for watched_list in user_data["friends"]:
        for movie_item in watched_list["watched"]:
            if movie_item not in friends_watched:
                friends_watched.append(movie_item)
    for movie_item in friends_watched:
        if movie_item["host"] in user_data["subscriptions"]:
            recommendations.append(movie_item)

    return recommendations

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    user_watched = get_unique_watched(user_data)
    recommendations = []

    for movie_item in friends_watched:
        if movie_item not in user_watched:
            if movie_item["genre"] == fav_genre:
                recommendations.append(movie_item)
    return recommendations

def get_rec_from_favorites(user_data):
    user_favs = user_data["favorites"]
    friends_watched =[]
    recommendations = []

    for watched_list in user_data["friends"]:
        for movie_item in watched_list["watched"]:
            if movie_item not in friends_watched:
                friends_watched.append(movie_item)

    for movie_item in user_favs:
        if movie_item not in friends_watched:
            recommendations.append(movie_item)

    return recommendations
