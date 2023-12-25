from list_movies import list_movies
from add_movie import add_movie
from find_movie import find_movie

print("*** Welcome to the Movie App ***")

MENU_PROMPT = "Enter 'A' to add a movie, 'L' to see your movies, 'F' to find a movie by title or 'Q' to quit: "

movies = []

selection = input(MENU_PROMPT).lower()

while selection != 'q':
    if selection == "a":
        add_movie(movies)
    elif selection == "l":
        if len(movies) == 0:
            print("The List in empty!")
        else:
            list_movies(movies)
    elif selection == "f":
        print(find_movie(movies))
    else:
        print("Unknown command, please try again.")

    selection = input(MENU_PROMPT).lower()

print("*** GOOD BYE ***")
