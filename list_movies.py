def list_movies(movies):
    return [print(
        f" {index + 1} - Title: {movie['title'].title()}, director: {movie['director'].title()}, release year :"
        f" {movie['year']}")
        for index, movie in enumerate(movies)]
