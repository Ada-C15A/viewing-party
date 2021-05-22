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
    if not user_data["watched"]:
        return 0

    total = 0.0 
    for movie in user_data["watched"]:
           total += movie["rating"]

    return total/len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    if not user_data["watched"]:
        return None
    
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    maximum = max(genre_count, key=genre_count.get) # get returns the value of the item with the specified key
    return maximum

def get_unique_watched(user_data):
    # give me the movies that the user has watched that the firends have not
    unique_watched = user_data["watched"].copy()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in unique_watched:
                unique_watched.remove(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # we need to iterate over the movies our firends have wathced, 
            # if a friend has watched the movie we need to check to see if the user has wathced it, if so, then keep going
            if movie in user_data["watched"]:
                continue
            # is this somthing we have already included in the unique list
            if movie in friends_unique_watched:
                continue
            # otherwise this movie is what the friend has watched and should be apart of the results 
            friends_unique_watched.append(movie)

    return friends_unique_watched


def get_available_recs(user_data):
    reccomendations = []
    friends_unique_movies = get_friends_unique_watched(user_data) # Determine a list of recommended movies.

    for movie in friends_unique_movies: # list of movies our friends have watched
        if movie["host"] in user_data["subscriptions"]:
            reccomendations.append(movie)

    return reccomendations


def get_new_rec_by_genre(user_data):
    reccomendations = []
    get_most_watched_genres = get_most_watched_genre(user_data) # most watched genre
    friends_unique_movies = get_friends_unique_watched(user_data) # list of movies our friends have watched

    for movie in friends_unique_movies: # list of movies our friends have watched
        if get_most_watched_genres in movie.values():
            reccomendations.append(movie)

    return reccomendations

def get_rec_from_favorites(user_data):
    reccomendations = []
    get_user_watched = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in get_user_watched:
            reccomendations.append(movie)

    return reccomendations
