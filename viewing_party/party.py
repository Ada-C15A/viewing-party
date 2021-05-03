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
        print
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)            
    return user_data
