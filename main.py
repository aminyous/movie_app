from list_movies import list_movies

print("*** Welcome to the Movie App ***")

movies = ["Movie_1", "Movie_2", "Movie_3"]

selection = input("Please enter 'A' for add, 'L' for show, 'Q' for quit").lower()

while selection != 'q':
    if selection == "a":
        pass
    elif selection == "l":
        list_movies(movies)
    elif selection == "q":
        break
    else:
        print("Your choice is not valid.")

    selection = input("Please enter 'A' for add, 'L' for show, 'Q' for quit").lower()

print("*** GOOD BYE ***")
