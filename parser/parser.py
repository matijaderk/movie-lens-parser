import movieHelper
import userHelper
import othersHelper
import os.path

MOVIES = "movies.csv"
GENRES = "genres.csv"
MOVIE_GENRES = "movie-genres.csv"
USERS = "users.csv"

RATINGS = "ratings.csv"
TAGS = "tags.csv"
LINKS = "links.csv"

INPUT_DIR = "../input/"
OUTPUT_DIR = "../output/"

# Dirs
current_dir = os.path.abspath(os.path.dirname(__file__))
input_dir = os.path.join(current_dir, INPUT_DIR)
output_dir = os.path.join(current_dir, OUTPUT_DIR)

# Input files
movies_file = os.path.join(input_dir, MOVIES)
ratings_file = os.path.join(input_dir, RATINGS)
tags_file = os.path.join(input_dir, TAGS)
links_file = os.path.join(input_dir, LINKS)

# Output files
movies_file_output = os.path.join(output_dir, MOVIES)
genres_file_output = os.path.join(output_dir, GENRES)
movie_genres_file_output = os.path.join(output_dir, MOVIE_GENRES)
users_file_output = os.path.join(output_dir, USERS)

movieHelper.parse_movie_file(movies_file, movies_file_output, genres_file_output, movie_genres_file_output)
userHelper.create_user_file(tags_file, ratings_file, users_file_output)
othersHelper.copy_other_files(RATINGS, TAGS, LINKS, input_dir, output_dir)