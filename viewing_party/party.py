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
            print('to watch list now: ', to_watch_list)
            watched_list.append(movie_dict)
    return user_data
    