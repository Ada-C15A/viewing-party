def create_movie(title, genre, rating):
    m = dict();
    m['title'] = title
    m['genre'] = genre
    m['rating'] = rating
    if m['title'] and m['genre'] and m['rating']:
        return m
    
def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title in movie['title']:
            user_data['watchlist'].remove(movie)
            add_to_watched(user_data, movie)
            return user_data
    return user_data
    
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) < 1:
        return 0.0
    movie_rating_total = 0
    for movie in user_data['watched']:
        movie_rating_total += movie['rating']
    return movie_rating_total / len(user_data['watched'])    

def get_most_watched_genre(user_data):
    movie_genre_dictionary = {}
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre_dictionary:
            movie['genre'] = 1
            print("HERE: " + str(movie_genre_dictionary))
            return movie_genre_dictionary 
        else:    
            movie['genre'] += 1
            print("NOW HERE: " + str(movie_genre_dictionary))
        return movie_genre_dictionary 
    