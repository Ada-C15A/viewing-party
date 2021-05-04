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
            print("HERE")
            return user_data
    return user_data
    



