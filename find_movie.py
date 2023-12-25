from print_movie import print_movie


def find_movie(movies):
    search_title = input("Enter movie title tou're looking for: ")
    for movie in movies:
        if movie["title"] == search_title or movie["title"].title() == search_title:
            return print_movie(movie)
