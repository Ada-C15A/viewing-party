def create_movie(movie_title, genre, rating):
   return {"title":movie_title, "genre":genre, "rating":rating} if (movie_title and genre and rating) else None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    wl = user_data["watchlist"]
    for item in wl:
        if item["title"] == title:
            add_to_watched(user_data,wl.pop(wl.index(item)))
    return user_data