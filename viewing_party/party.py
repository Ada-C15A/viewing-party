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
    uesr_watched_movie_rating = []
    # average_rating = (sum(watched_movie_rating) /len(watched_movie_rating))
    
    for movie in user_data["watched"]:
        uesr_watched_movie_rating.append(movie["rating"])
    if len(uesr_watched_movie_rating) == 0:
        return 0.0
    else:
        average_rating = sum(uesr_watched_movie_rating) /len(uesr_watched_movie_rating)

    return average_rating

def get_most_watched_genre(user_data):
    counter = 0
    most_genre_watched = ""
    genre_dict = {}
    
    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1

    for key, value in genre_dict.items():
        if counter < value:
            counter = value
            most_genre_watched = key            
    return most_genre_watched