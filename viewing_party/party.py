def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_details = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_details
    else:
        return None
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):    
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)            
    return user_data

#Wave-2
def get_watched_avg_rating(user_data):
    user_watched_movie_rating = []
    
    for movie in user_data["watched"]:
        user_watched_movie_rating.append(movie["rating"])
        
    if len(user_watched_movie_rating) == 0:
        return 0.0
    else:
        average_rating = sum(user_watched_movie_rating) /len(user_watched_movie_rating)

    return average_rating

def get_most_watched_genre(user_data):
    max_genre = 0
    most_genre_watched = ""
    genre_dict = {}
    
    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1

    for name, count_genre in genre_dict.items():
        if max_genre < count_genre:
            max_genre = count_genre
            most_genre_watched = name            
    return most_genre_watched

#wave-3
def get_friends_watch_list(user_data):
    friends_watched_list = []
    for friend in user_data["friends"]:
        for title in friend["watched"]:
            friends_watched_list.append(title)
    return friends_watched_list


def get_unique_watched(user_data):
    friends_watched_list = get_friends_watch_list(user_data)
    user_watched_list = []

    for user_movie in user_data["watched"]:
        if user_movie not in friends_watched_list:
            user_watched_list.append(user_movie)
    return user_watched_list

def get_friends_unique_watched(user_data):
    friends_list_movie = get_friends_watch_list(user_data)
    list_friends_unique_watched = []
    for title in friends_list_movie:
        if title not in user_data["watched"] and title not in list_friends_unique_watched:
            list_friends_unique_watched.append(title)
    return list_friends_unique_watched
