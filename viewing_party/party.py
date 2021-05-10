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
    new_dict = {}
    for genre in genre_list:
        new_dict[genre] = genre_list.count(genre)
    return genre
