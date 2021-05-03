def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None
    return {'title': movie_title,
            'genre': genre,
            'rating': rating
            }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data["watched"].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data
