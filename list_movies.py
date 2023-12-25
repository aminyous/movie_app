from print_movie import print_movie


def list_movies(movies):
    if len(movies) == 0:
        return print("The List in empty!")
    else:
        return [print(f"{index+1} - {print_movie(movie)}") for index, movie in enumerate(movies)]
