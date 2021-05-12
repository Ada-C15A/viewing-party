def create_movie(movie_title, genre, rating):
    if movie_title is None:
        return None
    elif genre is None:
        return None
    elif rating is None:
        return None
    else:
        return {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data
    

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def updated_data():
    pass

def get_watched_avg_rating(user_data):
    if user_data["watched"]
    pass