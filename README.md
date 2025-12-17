# Movie Database CLI

A command-line interface application for managing a personal movie collection. This interactive tool allows users to add, update, delete, search, and analyze movies with ratings and release years.

## Features

- **Movie Management**: Add, update, and delete movies from your collection
- **List & Browse**: View all movies with their details (title, year, rating)
- **Search**: Find movies by title with partial matching
- **Statistics**: Analyze your collection with average ratings, best/worst movies
- **Random Selection**: Get random movie recommendations from your collection
- **Sorting**: Order movies by rating or release year
- **Filtering**: Filter movies by minimum rating or year range
- **Persistent Storage**: Movies are saved and loaded automatically

## Prerequisites

### Required Files

- `movie_storage.py` - Storage module that handles movie data persistence and operations

### Python Version

- Python 3.6 or higher

## Installation

1. Clone or download the repository
2. Ensure `movie_storage.py` is in the same directory
3. Run the application:

```bash
python movie_app.py
```

## Usage

### Starting the Application

```bash
python movie_app.py
```

### Main Menu

Upon starting, you'll see the interactive menu:

Menu:  
0. Exit

1.  List movies
    
2.  Add movies
    
3.  Delete movies
    
4.  Update movies
    
5.  Stats
    
6.  Random movie
    
7.  Search movie
    
8.  Movies sorted by rating
    
9.  Movies sorted by year
    
10.  Filter movies
    

Enter choice (0-10):

## Commands

### 0. Exit
Closes the application gracefully.

**Usage:**
Enter choice (0-10): 0  
Bye!

### 1. List Movies
Displays all movies in your collection with their year and rating.

**Usage:**
Enter choice (0-10): 1

**Example Output:**
The Shawshank Redemption (1994): 9.3  
The Godfather (1972): 9.2  
The Dark Knight (2008): 9.0  
Inception (2010): 8.8

**Empty Collection:**
No movies yet

### 2. Add Movies
Add a new movie to your collection with title, year, and rating.

**Usage:**
Enter choice (0-10): 2  
Enter a title: Interstellar  
Enter the year of the movie: 2014  
Enter the rating of the movie: 8.6  
Movie Interstellar added

**Validation:**
- Title cannot be empty
- Year must be a valid integer
- Rating must be a valid number (float)

**Error Handling:**
Enter a title:  
Enter a valid title

Enter the year of the movie: abc  
Invalid number

### 3. Delete Movies
Remove a movie from your collection by title.

**Usage:**
Enter choice (0-10): 3  
Enter a movie to delete: Inception  
The title Inception deleted

**If Movie Not Found:**
Enter a movie to delete: NonExistent  
Movie NonExistent does not exists

### 4. Update Movies
Modify the rating of an existing movie.

**Usage:**
Enter choice (0-10): 4  
Enter a title to update: The Dark Knight  
Enter the new rating: 9.5  
Movie The Dark Knight updated

**Error Cases:**
Enter a title to update: Unknown Movie  
Movie Unknown Movie not found

Enter the new rating: abc  
Invalid number

### 5. Stats
Display statistical analysis of your movie collection.

**Usage:**
Enter choice (0-10): 5

**Expected Output** (implementation depends on `movie_storage.py`):
- Average rating
- Highest rated movie
- Lowest rated movie
- Total number of movies
- Other relevant statistics

### 6. Random Movie
Get a random movie suggestion from your collection.

**Usage:**
Enter choice (0-10): 6

**Expected Output:**
Displays a randomly selected movie from your database.

### 7. Search Movie
Search for movies by title (case-insensitive, partial matching).

**Usage:**
Enter choice (0-10): 7

You'll be prompted to enter a search term, and matching movies will be displayed.

### 8. Movies Sorted by Rating
Display all movies ordered by rating (highest to lowest or vice versa).

**Usage:**
Enter choice (0-10): 8

**Expected Output:**
Movies listed in rating order with their details.

### 9. Movies Sorted by Year
Display all movies ordered by release year.

**Usage:**
Enter choice (0-10): 9

**Expected Output:**
Movies listed chronologically with their details.

### 10. Filter Movies
Filter movies based on criteria (e.g., minimum rating, year range).

**Usage:**
Enter choice (0-10): 10

You'll be prompted for filter criteria, and matching movies will be displayed.

## Data Structure

Movies are stored with the following structure:

{  
"Movie Title": {  
"year": 2014,  
"rating": 8.6  
},  
"Another Movie": {  
"year": 2010,  
"rating": 9.0  
}  
}


## Architecture

### Main Components

1. **`menu_display()`**: Displays the interactive menu options
2. **`main()`**: Main application loop handling user input and command dispatch
3. **`movie_storage`**: External module handling data persistence and operations

### Design Pattern

The application uses a **menu-driven architecture**:
- Numbered menu options (0-10)
- Input validation with try/except blocks
- Continuous loop with "Press Enter to continue" prompts
- Modular separation between UI (this file) and data layer (`movie_storage`)

## movie_storage.py Interface

The application expects the following functions in `movie_storage.py`:

def get_movies() -> dict  
def add_movie(title: str, year: int, rating: float) -> None  
def delete_movie(title: str) -> None  
def update_movie(title: str, rating: float) -> None  
def stats() -> None  
def random_movie() -> None  
def search_movie() -> None  
def sorted_by_rating() -> None  
def sorted_by_year() -> None  
def filter_movie() -> None

## Features by Category

### Data Management
- ✅ Add new movies
- ✅ Delete existing movies
- ✅ Update movie ratings
- ✅ List all movies

### Discovery & Analysis
- ✅ Search by title
- ✅ Random recommendations
- ✅ Statistical analysis
- ✅ Sort by rating
- ✅ Sort by year
- ✅ Filter by criteria

### User Experience
- ✅ Interactive menu
- ✅ Input validation
- ✅ Error handling
- ✅ Clear feedback messages
- ✅ Pause between operations

## Limitations

- **Title as Primary Key**: Movie titles must be unique (no duplicates)
- **Simple Search**: Search functionality depends on `movie_storage` implementation
- **No Undo**: Deletions and updates are immediate with no undo option
- **Limited Movie Metadata**: Only stores title, year, and rating (no director, genre, etc.)
- **No Data Export**: Cannot export collection to external formats

## Future Enhancements

### Potential Features
- **Extended Metadata**: Add director, genre, cast, runtime, plot summary
- **Multiple Ratings**: Support different rating systems (IMDb, Rotten Tomatoes, personal)
- **Watch Status**: Track watched/unwatched status and watch dates
- **Tags & Collections**: Organize movies into custom categories
- **Data Import/Export**: CSV, JSON export and import capabilities
- **API Integration**: Fetch movie data from IMDb, TMDb, or OMDb APIs
- **Recommendations**: Suggest similar movies based on ratings
- **Batch Operations**: Add/delete/update multiple movies at once
- **Notes & Reviews**: Add personal notes and reviews to movies
- **Watchlist**: Separate list for movies to watch

### Code Improvements
- **Configuration File**: Customize menu options and display preferences
- **Logging**: Track all operations for debugging
- **Unit Tests**: Comprehensive test coverage
- **Command-Line Arguments**: Support non-interactive mode
- **Colorized Output**: Enhanced visual presentation
- **Input History**: Navigate previous inputs with arrow keys
- **Confirmation Prompts**: Confirm destructive operations (delete, update)

## Troubleshooting

### "No movies yet" on List
- You haven't added any movies yet
- Use option 2 to add your first movie

### "Invalid choice"
- Enter only numbers between 0-10
- Avoid letters or special characters

### "Movie does not exists"
- Check spelling of movie title
- Use option 1 to list all movies
- Titles are case-sensitive

### "Invalid number"
- Year must be a whole number (e.g., 2014)
- Rating can be decimal (e.g., 8.5)
- Don't include text or special characters

## Best Practices

### Adding Movies
- Use full movie titles for clarity
- Include release year, not re-release dates
- Use consistent rating scale (e.g., 0-10)

### Rating System
- Recommend using 0-10 scale for consistency
- Be consistent with decimal places (e.g., always use .0 or .5)

### Organization
- Regularly review and update ratings
- Delete duplicate or test entries
- Use filters to manage large collections

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Areas for improvement:
- Enhanced search capabilities
- Additional sorting/filtering options
- Better error messages
- UI improvements
- Performance optimizations
- Test coverage

## Support

For issues or questions:
- Verify `movie_storage.py` is properly implemented
- Check that all required functions exist
- Ensure data file permissions are correct
- Review error messages for specific issues

---

**Note**: This application requires the `movie_storage.py` module to handle data persistence. Ensure this module is properly implemented with all required functions before running the application.

