from print_movie import print_movie


def find_movie(movies):
    search_title = input("Enter movie title you're looking for: ")
    for movie in movies:
        if movie["title"] == search_title:
            print(print_movie(movie))


