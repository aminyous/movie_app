def add_movie(movies):
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


