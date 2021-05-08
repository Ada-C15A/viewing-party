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
            # watched_movie = movie
            add_to_watched(user_data, movie)
    i = 0
    while i < len(user_data["watchlist"]):
        if user_data["watchlist"][i]["title"] == watch_title:
            user_data["watchlist"].pop(i)
        i += 1
    return user_data
