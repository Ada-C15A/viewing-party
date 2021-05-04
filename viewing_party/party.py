def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title":title, "genre":genre, "rating":rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0
    else:
        total = 0
        for movie in user_data['watched']:
            total += movie['rating']
        return total/len(user_data['watched'])

def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched = None
    if len(user_data['watched']) == 0:
        return None
    for movie in user_data['watched']:
        if movie['genre'] in genre_count:
            genre_count[movie['genre']] += 1
        else:
            genre_count[movie['genre']] = 1
    for key, value in genre_count.items():
        if not most_watched or genre_count[most_watched] < value:
            most_watched = key
    return most_watched

def get_unique_watched(user_data):
    unique_watched = [] + user_data['watched']

    for friend in user_data['friends']:
        for i in range(len(friend['watched'])):
            if friend['watched'][i] in unique_watched:
                unique_watched.remove(friend['watched'][i])

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    for friend in user_data['friends']:
        for i in range(len(friend['watched'])):
            if (friend['watched'][i] not in user_data['watched'] and
            friend['watched'][i] not in friends_unique_watched):
                friends_unique_watched.append(friend['watched'][i])

    return friends_unique_watched

def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    available_recs = []
    for unique_movie in friends_unique_watched:
        if unique_movie['host'] in user_data['subscriptions']:
            available_recs.append(unique_movie)

    return available_recs

def get_new_rec_by_genre(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    new_rec_by_genre = []
    most_watched_genre = get_most_watched_genre(user_data)
    for unique_movie in friends_unique_watched:
        if unique_movie['genre'] == most_watched_genre:
            new_rec_by_genre.append(unique_movie)

    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    rec_from_favorites = []
    favorites = user_data['favorites']

    for unique_movie in unique_watched:
        if unique_movie in favorites:
            rec_from_favorites.append(unique_movie)
    return rec_from_favorites

