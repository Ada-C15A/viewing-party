#list of disctionaries, where the inner dictionaries represent movies,
#and have keys: title, genre, and rating 
movies =[]

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
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

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0
    ratings = [movie['rating'] for movie in user_data["watched"]]
    return sum(ratings) / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genres = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie['genre'] in genres.keys():
            genres[movie['genre']] += 1
        else:
            genres[movie['genre']] = 1
        winners = [genre for genre, count in genres.items() if count == max(genres.values())]   
    return winners[0]