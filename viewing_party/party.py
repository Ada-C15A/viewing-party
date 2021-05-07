def create_movie(title, genre, rating):
    new_movie = {
        "title" : title,
        "genre" : genre,
        "rating" : rating,
    }

    # != and "is not" do the same
    if title != None and \
        genre != None and \
        rating != None:
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for movie_in_question in user_data["watchlist"]:
        if movie_in_question["title"] == title:
            user_data["watchlist"].remove(movie_in_question)
            user_data["watched"].append(movie_in_question)
    return user_data

