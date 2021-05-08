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
    for friend_watched in user_data["watchlist"]:
        if friend_watched["title"] == title:
            user_data["watchlist"].remove(friend_watched)
            user_data["watched"].append(friend_watched)
    return user_data

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) < 1:
        return 0
    else:
        total_ratings = 0
        for friend_watched in user_data["watched"]:
            total_ratings += friend_watched["rating"]
    return total_ratings/len(user_data["watched"])

def get_most_watched_genre(user_data):
    popular_genre = {}
    for friend_watched in user_data["watched"]:
        if friend_watched["genre"] not in popular_genre:
            popular_genre[friend_watched["genre"]] = 1
        else:
            popular_genre[friend_watched["genre"]] += 1
    # Question for later
    # max_key = max(popular_genre, key=popular_genre.get)
    # return max_key
    max_count = 0
    pop_genre = None
    for genre in popular_genre:
        count = popular_genre[genre]
        if count > max_count:
            max_count = count
            pop_genre = genre
    return pop_genre

def get_unique_watched(user_data):
  options_to_watch = []
  friends_watched = []
  for friend_watched in user_data["friends"]:
    for movie_watched in friend_watched["watched"]:
        if movie_watched not in friends_watched:
            friends_watched.append(movie_watched)

  for user_watched in user_data["watched"]:
      if user_watched not in friends_watched:
        options_to_watch.append(user_watched)
  return options_to_watch

def get_friends_unique_watched(user_data):
    options_to_watch = []
    user_already_watched = []
    for user_watched in user_data["watched"]:
        user_already_watched.append(user_watched)
    print(user_already_watched)
    
    for friend_watched in user_data["friends"]:
        for movie_watched in friend_watched["watched"]:
            if movie_watched not in user_already_watched and \
                movie_watched not in options_to_watch:

                options_to_watch.append(movie_watched)
    return options_to_watch

def get_available_recs(user_data):
  recommended = []
  for friend_watch in user_data["friends"]:
    for item_watched in friend_watch["watched"]:
      if item_watched not in user_data["watched"] and \
          item_watched["host"] in user_data["subscriptions"]:
        if item_watched not in recommended:
            recommended.append(item_watched)
  return recommended

def get_new_rec_by_genre(user_data):
  user_pop_genre = ""
  popular_genre = {}
  recommended = []

  for user_watched in user_data["watched"]:
    if user_watched["genre"] not in popular_genre:
      popular_genre[user_watched["genre"]] = 1
    else:
      popular_genre[user_watched["genre"]] += 1

  max_count = 0
  pop_genre = None
  for genre in popular_genre:
    count = popular_genre[genre]
    if count > max_count:
      max_count = count
      pop_genre = genre

  user_pop_genre = pop_genre

  for friend_watched in user_data["friends"]:
    for friends_watched_movie in friend_watched["watched"]:
      if friends_watched_movie not in user_data["watched"] and \
          friends_watched_movie["genre"] == user_pop_genre:
        recommended.append(friends_watched_movie)
  return recommended

def get_rec_from_favorites(user_data):
  friends_movies = []
  recommended = []

  for friends_movie in user_data["friends"]:
    for watched_movie in friends_movie["watched"]:
      if watched_movie not in friends_movies:
        friends_movies.append(watched_movie)

  for user_fav in user_data["favorites"]:
    if user_fav not in friends_movies:
      recommended.append(user_fav)
  return recommended