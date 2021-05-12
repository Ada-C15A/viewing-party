def create_movie(title, genre, rating):

  if title and genre and rating:
    movie = {}
    movie['title'] = title
    movie['genre'] = genre
    movie['rating'] = rating

    return movie

  return None


def add_to_watched(user_data, movie):
  #add entire movie object to user_data
  user_data['watched'].append(movie)
  return user_data

def add_to_watchlist(user_data, movie):
  user_data['watchlist'].append(movie)
  return user_data

def watch_movie(user_data, title):

  for movie in user_data['watchlist']:
    if title == movie['title']:
      user_data['watchlist'].remove(movie)
      return add_to_watched(user_data, movie)
  return user_data


#If the title is in a movie in the user's watchlist:
# remove that movie from the watchlist
# add that movie to watched
# return the user_data
# If the title is not a movie in the user's watchlist:
# return the user_data

def get_watched_avg_rating(user_data):
    watched_ratings = []
    for movie in user_data['watched']:
      watched_ratings.append(movie['rating'])

    if len(watched_ratings) == 0:
      return 0.0
    
    avg_rating = sum(watched_ratings)/len(watched_ratings)

    return avg_rating

def get_most_watched_genre(user_data):
    watched_genres = []
    for movie in user_data['watched']:
      watched_genres.append(movie['genre'])

    if len(watched_genres) == 0:
      return None

    return max(set(watched_genres), key = watched_genres.count)

def get_unique_watched(user_data):
    unique_watched = [] + user_data['watched']

    for friend in user_data['friends']:
      for movie in friend['watched']:
        if movie in unique_watched:
          unique_watched.remove(movie)
    return unique_watched


def get_friends_unique_watched(user_data):
  friends_unique_watched = []

  for friend in user_data['friends']:
    for watched in friend['watched']:
      if watched not in user_data['watched'] and watched not in friends_unique_watched:
        # print('appending watch title', watched['title'])
        friends_unique_watched.append(watched)
  # print("what am i return", friends_unique_watched)
  return friends_unique_watched


def get_available_recs(user_data):
  recommended_movies = []
  possible_movies = get_friends_unique_watched(user_data)

  for movie in possible_movies:
    if movie['host'] in user_data['subscriptions']:
      recommended_movies.append(movie)
    
  return recommended_movies

def get_new_rec_by_genre(user_data):
  recommended_movies = []
  possible_movies = get_friends_unique_watched(user_data)
  favorite_genre = get_most_watched_genre(user_data)

  for movie in possible_movies:
    if movie['genre'] == favorite_genre:
      recommended_movies.append(movie)
    
  return recommended_movies


def get_rec_from_favorites(user_data):
  favorite = []
  possible_movies = get_unique_watched(user_data)

  for movie in possible_movies:
    if movie in user_data['favorites']:
      favorite.append(movie)
  return favorite