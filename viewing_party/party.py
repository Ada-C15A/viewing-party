def create_movie(movie_title, genre, rating):
   return {"title":movie_title, "genre":genre, "rating":rating} if (movie_title and genre and rating) else None