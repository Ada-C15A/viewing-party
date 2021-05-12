def create_movie(movie_title, genre, rating):
   return {"title":movie_title, "genre":genre, "rating":rating} if (movie_title and genre and rating) else None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    wl = user_data["watchlist"]
    for item in wl:
        if item["title"] == title:
            add_to_watched(user_data,wl.pop(wl.index(item)))
    return user_data

def get_watched_avg_rating(user_data):
    cumulative_ratings = 0
    watched = user_data["watched"]
    for item in watched:
        cumulative_ratings += item["rating"]

    return cumulative_ratings/len(watched) if len(watched) > 0 else 0

def get_most_watched_genre(user_data):
    counts = {}
    watched = user_data["watched"]
    popular = ['',0]
    for item in watched:
        this_genre_count = item["genre"]
        if this_genre_count not in counts:
            counts[this_genre_count] = 1
        else:
            counts[this_genre_count] += 1
        if counts[this_genre_count] > popular[1]:
            popular[0] = this_genre_count
            popular[1] = counts[this_genre_count]

    return popular[0] if popular[1] > 0 else None

def get_unique_watched(user_data):
    unique = []
    watched = user_data["watched"]

def get_available_recs(user_data):
    user_watched = user_data["watched"]
    subscriptions = user_data["subscriptions"]
    recs = []
    for friend in user_data["friends"]:
        for item in friend["watched"]:
            if item not in user_watched and item["host"] in subscriptions and item not in recs:
                recs.append(item)

    return recs

def get_new_rec_by_genre(user_data):
    user_watched = user_data["watched"]
    num_watched = len(user_watched)
    recs = []
    if num_watched > 0:
        genres = {}
        top_genre = ""
        curr_top = ['',0]
        for i in range(num_watched):
            current = user_watched[i]["genre"]
            if current not in genres:
                genres[current] = 1
            else:
                genres[current] += 1
                if genres[current] > curr_top[1]:
                    top_genre = current
                    curr_top[0] = current
                    curr_top[1] = genres[current]

        for friend in user_data["friends"]:
            for item in friend["watched"]:
                if (item["title"] not in user_watched) and item["genre"] == top_genre:
                    recs.append(item)

    return recs

def get_rec_from_favorites(user_data):
    favs = user_data["favorites"]
    friends = user_data["friends"]
    recs = []
    for i in range(len(favs)):
        friend_watched = False
        for friend in friends:
            for watched in friend["watched"]:
                if watched["title"] == favs[i]["title"]:
                    friend_watched = True
        if not friend_watched:
            recs.append(favs[i])

    return recs
