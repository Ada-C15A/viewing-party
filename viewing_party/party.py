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


def get_watched_avg_rating(user_data):
    if user_data['watched']:
        total = 0
        for movie in user_data['watched']:
            total += movie['rating']
        return total/len(user_data['watched'])
    else:
        return 0


def get_most_watched_genre(user_data):
    if len(user_data['watched']) == 0:
        return None
    watched_count = {}
    most_watched = [user_data['watched'][0]['title'], 1]
    for movie in user_data['watched']:
        print(movie)
        if movie['genre'] in watched_count:
            watched_count[movie['genre']] += 1
        else:
            watched_count[movie['genre']] = 1
        if watched_count[movie['genre']] > most_watched[1]:
            most_watched[0] = movie['genre']
            most_watched[1] = watched_count[movie['genre']]
    return most_watched[0]


def get_unique_watched(user_data):
    unique_watched = []
    for movie in user_data["watched"]:
        isInFriendsList = False
        for friends_movies in user_data['friends']:
            for individual in friends_movies['watched']:
                if individual['title'] == movie['title']:
                    isInFriendsList = True
        if isInFriendsList == False:
            unique_watched.append(movie)
    return unique_watched


def get_friends_unique_watched(user_data):
    unique_watched = []
    seen = set()

    for user_watched_movie in user_data['watched']:
        seen.add(user_watched_movie['title'])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in seen:
                unique_watched.append(movie)
                seen.add(movie["title"])
    return unique_watched


