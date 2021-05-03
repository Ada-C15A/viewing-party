#list of disctionaries, where the inner dictionaries have keys: title, genre, and rating 
movies =[]

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    
    movies.append({"title": title, "genre": genre, "rating": rating})    
    return movies.pop()

def add_to_watched(user_data, movie):
    user_data["watched"].append({"title": movie["title"], "genre": movie["genre"], "rating": movie["rating"]})
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append({"title": movie["title"], "genre": movie["genre"], "rating": movie["rating"]})
    return user_data

def watch_movie(user_data, title):
    movie = next((movie for movie in user_data["watchlist"] if movie['title'] == title), None) 
    if movie ==    None:
        return user_data 
    
    user_data["watched"].append(movie)
    user_data["watchlist"] = [movie for movie in user_data["watchlist"] if not (movie['title'] == title)]
    return user_data 