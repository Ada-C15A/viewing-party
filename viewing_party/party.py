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