def create_movie(movie_title, genre, rating):
   return {"title":movie_title, "genre":genre, "rating":rating} if (movie_title and genre and rating) else None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            movie = user_data["watchlist"].pop(user_data["watchlist"].index(item))
            add_to_watched(user_data,movie)
    return user_data