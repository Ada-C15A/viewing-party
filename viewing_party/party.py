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
    if len(user_data['watched']) < 1:
        return None
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre_dictionary.keys():
            movie_genre_dictionary[movie['genre']] = 1

        else:
            movie_genre_dictionary[movie['genre']] += 1

    most_watched = sorted(movie_genre_dictionary, key=movie_genre_dictionary.get)
    print(movie_genre_dictionary)
    print(most_watched[-1])
    return most_watched[-1]  
   

    