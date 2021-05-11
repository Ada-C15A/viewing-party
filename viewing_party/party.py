def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
        
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_list = user_data["watched"]
    to_watch_list = user_data["watchlist"]
    for movie_dict in to_watch_list:
        if movie_dict["title"] == title:
            to_watch_list.remove(movie_dict)
            watched_list.append(movie_dict)
    return user_data
  
def get_watched_avg_rating(user_data):
    users_watched_list = user_data["watched"]
    ratings_list = []
    if len(users_watched_list) == 0:
        return 0.0
    for movie in users_watched_list:
        movie_rating = movie["rating"]
        ratings_list.append(movie_rating)
        average_rating = sum(ratings_list)/len(ratings_list)
    return average_rating

def get_most_watched_genre(user_data):
    watched_movie_data = user_data["watched"]
    genre_list = []
    if len(watched_movie_data) == 0:
        return None
    for movie in watched_movie_data:
        genre_of_movie = movie["genre"]
        genre_list.append(genre_of_movie)
    genre_count = {}
    for genre in genre_list:
        genre_count[genre] = genre_list.count(genre)
    most_watched_genre = max(genre_count, key=genre_count.get)
    return most_watched_genre

def get_unique_watched(user_data):
    friends_watched_list = []
    users_unique_watched_list = []
    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friends_watched_list.append(movie["title"])
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_list:
            users_unique_watched_list.append(movie)
    return users_unique_watched_list

def get_friends_unique_watched(user_data):
    friends_watched_list = []
    friends_unique_watched_list = []
    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    for i in range(len(friends_watched_list)):
        if friends_watched_list[i] not in user_data["watched"]:
            friends_unique_watched_list.append(friends_watched_list[i])
    return friends_unique_watched_list

def get_available_recs(user_data):
    friends_watched_list = []
    reccomendations = []
    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    for movie in friends_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            reccomendations.append(movie)
    return reccomendations

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    user_watched = get_unique_watched(user_data)
    reccomendations = []

    for movie in friends_watched:
        if movie not in user_watched:
            if movie["genre"] == most_watched_genre:
                reccomendations.append(movie)
    return reccomendations

def get_rec_from_favorites(user_data):
    friends_watched = []
    reccomendations = []
    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friends_watched.append(movie)
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            reccomendations.append(movie)
    return reccomendations
