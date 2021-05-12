def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
                "title": title,
                "genre": genre,
                "rating": rating
        }
    else:
        return None

def add_to_watched(user_data , movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data , movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data , title):
# checks if movie title is in watchlist
# if it's remove from watchlist
# and add movie to watched list
#  return the user_data
# if movie is not in the watchlist return the user_data
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie = user_data["watchlist"].pop(i)
            return add_to_watched(user_data,movie)

    return user_data

def get_watched_avg_rating(user_data):
    sum_num = 0
    movie_list = user_data["watched"]
    for movie in movie_list:
        sum_num = sum_num + movie["rating"]
    if len(movie_list) == 0:
        return 0.0
    avg = sum_num / len(movie_list)
    return avg

def get_most_watched_genre(user_data):
	""" Returns the genre that is most watched. Assuming there is no ties for most watched.
	"""
	count_genres = {}
	most_watched_genre = ""
	highest_count = 0
	# movie_list = [{"genre": "Horror"},{"genre": "Action"},{"genre": "Horror"}]	
	movie_list = user_data["watched"]

	if len(movie_list) == 0:
		return None
	for movie in movie_list:
		genre = movie["genre"]
		""" In each iteration movie takes on the value of each element in the movie_list.
			Ex. Iteration 0: 
			    movie = {"genre": "Horror"}
			    genre = "Horror"
			    Iteration 1:
			    movie = {"genre": "Action"}
				genre = "Action"
				ETC
		"""
		if genre in count_genres:
			""" Assume "Horror" is an existing key in count_genres
			    count_genres = {
					"Horror": 1,
					"Action": 1
			    } 
				Ex. Iteration 3
					movie = {"genre": "Horror"}
			    	genre = "Horror"
			"""
			count_genres[genre] += 1
		else:
			count_genres[genre] = 1
		if count_genres[genre] > highest_count:
			most_watched_genre = genre
			highest_count = count_genres[genre]
	return most_watched_genre

def get_unique_watched(user_data):
    """ user_data dict with watched list of movies dictionaries and friends
    user_data = {
        watched[movies{title:}],
        friends[friend{watched[movies{title:}]}]                  
    }
    """
    """
movies that user has watched
movies that friend has watched
which movies the user has watched but none friends watched  movies user watch != movies friends watched 
return unique[movies{}]
    """
    unique_movies = []

    movie_list = user_data["watched"]
    friends_list = user_data["friends"]

    for movie in movie_list:
        title = movie["title"]
        unique = True
        for friend in friends_list:
            friend_movies_list = friend["watched"]
            for friend_movie in friend_movies_list:
                if friend_movie["title"] == title:
                    unique = False
                    break
            if not unique:
                break
        if unique:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    unique_movies = []
    movie_list = user_data["watched"]
    friends_list = user_data["friends"]

    for friend in friends_list:
        friend_movies_list = friend["watched"]
        for friend_movie in friend_movies_list:
            title = friend_movie["title"]
            unique = True    
            for movie in movie_list:
                if movie["title"] == title:
                    unique = False
                    break
            if unique and friend_movie not in unique_movies:
                unique_movies.append(friend_movie)

    return unique_movies

def get_available_recs(user_data):
    """user_data
    {    subscriptions["name, name , name"]}
    """
    unique_movies = []
    movie_list = user_data["watched"]
    friends_list = user_data["friends"]

    for friend in friends_list:
        friend_movies_list = friend["watched"]
        for friend_movie in friend_movies_list:
            title = friend_movie["title"]
            unique = True    
            for movie in movie_list:
                if movie["title"] == title:
                    unique = False
                    break
            if unique and friend_movie not in unique_movies and friend_movie["host"] in user_data["subscriptions"]:
                unique_movies.append(friend_movie)

    return unique_movies


def get_new_rec_by_genre(user_data):
    unique_movies = []
    movie_list = user_data["watched"]
    friends_list = user_data["friends"]
    genre = get_most_watched_genre(user_data)

    for friend in friends_list:
        friend_movies_list = friend["watched"]
        for friend_movie in friend_movies_list:
            title = friend_movie["title"]
            unique = True    
            for movie in movie_list:
                if movie["title"] == title:
                    unique = False
                    break
            if unique and friend_movie not in unique_movies and friend_movie["genre"] == genre:
                unique_movies.append(friend_movie)

    return unique_movies

def get_rec_from_favorites(user_data):
    unique_movies = []

    movie_list = user_data["favorites"]
    friends_list = user_data["friends"]

    for movie in movie_list:
        title = movie["title"]
        unique = True
        for friend in friends_list:
            friend_movies_list = friend["watched"]
            for friend_movie in friend_movies_list:
                if friend_movie["title"] == title:
                    unique = False
                    break
            if not unique:
                break
        if unique:
            unique_movies.append(movie)

    return unique_movies

