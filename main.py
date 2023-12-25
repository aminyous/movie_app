from list_movies import list_movies
from add_movie import add_movie
from find_movie import find_movie

print("*** Welcome to the Movie App ***")

MENU_PROMPT = "Enter 'A' to add a movie, 'L' to see your movies, 'F' to find a movie by title or 'Q' to quit: "

movies = []

selection = input(MENU_PROMPT).lower()

""" 
Using first class function to improve user selection menu 
"""

user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}

while selection != 'q':
    if selection in user_options:
        selected_function = user_options[selection]
        selected_function(movies)
    else:
        print("Unknown command, please try again.")

    selection = input(MENU_PROMPT).lower()

print("*** GOOD BYE ***")
