def create_movie(title, genre, rating):
    movies_dict = {
        "title" : title,
        "genre" : genre,
        "rating" : rating,
    }
    
    # != and "is not" do the same
    if title != None and \
        genre != None and \
        rating != None:
        return movies_dict