import json
import random

FILENAME = "data.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    try:
        with open(FILENAME, "r") as f:
            text = f.read().strip()
        if not text:
            return {}
        data = json.loads(text)
        if not isinstance(data, dict):
            return {}
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(FILENAME, "w") as f:
        json.dump(movies, f, indent=2, ensure_ascii=False)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if movies is None:
        return
    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    del movies[title]
    save_movies(movies)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    rec = movies.get(title)
    if rec is None:
        return
    rec["rating"] = rating
    save_movies(movies)


def sorted_by_rating():
    """Sort movies by their ratings"""
    movies = get_movies()
    rating = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for title, record in rating:
        print(f"{title} ({record.get('year')}): ({record.get('rating')})")


def sorted_by_year():
    """Sort movies in chronological order"""
    movies = get_movies()
    name = input("Do you want the latest movies first? (Y/N): ").strip().lower()
    if name == "y":
        movies_sorting = sorted(
            movies.items(), key=lambda x: x[1]["year"], reverse=True
        )
        for title, record in movies_sorting:
            year = record.get("year")
            rating = record.get("rating")
            print(f"{title} ({year}): {rating}")
    elif name == "n":
        movies_sorting = sorted(movies.items(), key=lambda x: x[1]["year"])
        for title, record in movies_sorting:
            year = record.get("year")
            rating = record.get("rating")
            print(f"{title} ({year}): {rating}")


def random_movie():
    """Select a random movie from the dictionaries"""
    movies = get_movies()
    title, rating = random.choice(list(movies.items()))
    print(f"Your movie for tonight: {title}, it's rated {rating['rating']}")


def prompt_float(prompt):
    """Keep asking until a number or blank (returns None)"""
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            return float(s)
        except ValueError:
            print("Please enter a number or leave it blank")


def prompt_int(prompt):
    """Keep asking until integer or blank (returns None)."""
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            return int(s)
        except ValueError:
            print("Please enter a number or leave it blank")


def filter_movie():
    """
    Filter the list of movies based on the provided criteria
    """
    movies = get_movies()
    min_rating = prompt_float(
        "Enter minimum rating (leave blank for no minimum rating): "
    )
    start_year = prompt_int("Enter start year (leave blank for no start year): ")
    end_year = prompt_int("Enter end year (leave blank for no end year): ")
    matches = []
    for title, record in movies.items():
        year = record.get("year")
        rating = record.get("rating")
        if min_rating is not None and rating < min_rating:
            continue
        if start_year is not None and year < start_year:
            continue
        if end_year is not None and year > end_year:
            continue
        matches.append((title, record))
    if not matches:
        print("No movies watched")
        return
    print()
    print("Filtered Moives:")
    for title, record in matches:
        year = record.get("year")
        rating = record.get("rating")
        print(f"{title} ({year}): {rating}")


def stats():
    """Finding the avg, the median the best movie and the worst movie"""
    movies = get_movies()
    ratings = []
    for record in movies.values():
        rating = record.get("rating")
        if isinstance(rating, (int, float)):
            ratings.append(float(rating))
    if not ratings:
        print("No numeric ratings found")
        return
    avg = sum(ratings) / len(ratings)
    ratings.sort()
    n = len(ratings)
    mid = n // 2
    if n % 2 == 1:
        median = ratings[mid]
    else:
        median = (ratings[mid - 1] + ratings[mid]) / 2
    best_rating = ratings[-1]
    worst_rating = ratings[0]
    best_title = [
        title for title, record in movies.items() if record.get("rating") == best_rating
    ]
    worst_title = [
        title
        for title, record in movies.items()
        if record.get("rating") == worst_rating
    ]
    print(f"Average rating: {avg:.1f}")
    print(f"Median rating: {median}")
    print(f"Best {', '.join(best_title)}: {best_rating}")
    print(f"Worst {', '.join(worst_title)}: {worst_rating}")


def search_movie():
    movies = get_movies()
    name = input("Enter part of movie name: ").lower()
    for title, record in movies.items():
        rating = record.get("rating")
        if name in title.lower():
            print(f"{title}, {rating}")
