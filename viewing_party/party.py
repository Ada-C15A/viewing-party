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
