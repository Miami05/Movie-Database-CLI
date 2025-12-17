import movie_storage


def menu_display():
    """Print the interactive menu options."""
    print()
    print("Menu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movies")
    print("3. Delete movies")
    print("4. Update movies")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Movies sorted by year")
    print("10. Filter movies")


def main():
    """Run the interactive Movies CLI.
    Shows a numbered menu (0–10), reads the user's choice, and dispatches to the
    corresponding handlers (list/add/delete/update/stats/random/search/sort/filter).
    Input of non-integer choices is handled with a simple error message, choosing 0
    exits the program.
    """
    while True:
        menu_display()
        try:
            print()
            num = int(input("Enter choice (0-10): "))
            print()
        except ValueError:
            print("Invalid choice")
            continue
        if num == 0:
            print("Bye!")
            break
        elif num == 1:
            movies = movie_storage.get_movies()
            if not movies:
                print("No movies yet")
            else:
                for title, record in movies.items():
                    year = record.get("year")
                    rating = record.get("rating")
                    print(f"{title} ({year}): {rating}")
        elif num == 2:
            title = input("Enter a title: ")
            if not title:
                print("Enter a valid title")
                continue
            try:
                year = int(input("Enter the year of the movie: "))
                rating = float(input("Enter the rating of the movie: "))
                movie_storage.add_movie(title, year, rating)
                print(f"Movie {title} added")
            except ValueError:
                print("Invalid number")
                print()
                continue
        elif num == 3:
            title = input("Enter a movie to delete: ")
            try:
                movie_storage.delete_movie(title)
                print(f"The title {title} deleted")
            except KeyError:
                print(f"Movie {title} does not exists")
        elif num == 4:
            title = input("Enter a title to update: ")
            db = movie_storage.get_movies()
            if title not in db:
                print(f"Movie {title} not found")
                continue
            try:
                rating = float(input("Enter the new rating: "))
            except ValueError:
                print("Invalid number")
                continue
            movie_storage.update_movie(title, rating)
            print(f"Movie {title} updated")
        elif num == 5:
            movie_storage.stats()
        elif num == 6:
            movie_storage.random_movie()
        elif num == 7:
            movie_storage.search_movie()
        elif num == 8:
            movie_storage.sorted_by_rating()
        elif num == 9:
            movie_storage.sorted_by_year()
        elif num == 10:
            movie_storage.filter_movie()
        print()
        input("Press Enter to continue")


if __name__ == "__main__":
    main()
