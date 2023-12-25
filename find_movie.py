def find_movie(title, movies):
    for movie in movies:
        if movie["title"] == title:
            return f"The movie found is : " \
                   f"Title : {movie['title']}, director: {movie['director']}, release year: {movie['year']}."
