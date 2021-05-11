def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, watch_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == watch_title:
            add_to_watched(user_data, movie)
    i = 0
    while i < len(user_data["watchlist"]):
        if user_data["watchlist"][i]["title"] == watch_title:
            user_data["watchlist"].pop(i)
        i += 1
    return user_data

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0
    avg_list = []
    for movie in user_data["watched"]:
        avg_list.append(movie["rating"])
    avg_list_total = sum(avg_list)
    avg_rating = avg_list_total / len(avg_list)
    return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) < 1:
        return None
    genre_dict = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]

        try:
            genre_dict[genre] += 1
        except:
            genre_dict[genre] = 1

    highest_val = 0
    for genre, value in genre_dict.items():
        if value > highest_val:
            highest_val = value
            most_watched_genre = genre

    return most_watched_genre

def get_unique_watched(user_data):
    unique_list = []
    friends_watched = []
    flat_friends_watchlist = []

    for friend in user_data["friends"]:
        watched = friend['watched']
        friends_watched.append(watched)
    flat_friends_watchlist = sum(friends_watched, [])

    for watched in user_data['watched']:
        if watched not in flat_friends_watchlist:
            unique_list.append(watched)

    return unique_list

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    friends_watched = []
    flat_friends_watchlist = []

    for friend in user_data["friends"]:
        watched = friend['watched']
        friends_watched.append(watched)
    flat_friends_watchlist = sum(friends_watched, [])

    for friend_watched in flat_friends_watchlist:
        if friend_watched not in user_data["watched"] and friend_watched not in friends_unique_list:
            friends_unique_list.append(friend_watched)

    return friends_unique_list

def get_available_recs(user_data):
    available_recs = []
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    
    return available_recs

def get_new_rec_by_genre(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    genre_recs = []

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            genre_recs.append(movie)

    return genre_recs

def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)
    recs_from_favorites = []

    for favorite in user_favorites:
        if favorite in unique_watched:
            recs_from_favorites.append(favorite)

    return recs_from_favorites
