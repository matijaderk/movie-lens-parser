import csv


def parse_genres(genres):
    genres_list = genres.split('|')
    return set(genres_list)


def parse_name_and_year(name_year):
    name = name_year[0:-6]
    year = name_year[-5:-1]
    if(year.isdigit()):
        return name, year

    return name, '2000'


def create_movie_genres(movie_id, movie_genres):
    movie_genre_list = []
    for genre in movie_genres:
        if genre not in ['(no genres listed)']:
            movie_genre_list.append((movie_id.strip(), genre.strip()))
    return movie_genre_list


def write_movie_genres(movie_genres_list, genres_list, writer):
    movie_genre_ids = []
    for mg in movie_genres_list:
        movie_genre_ids.append((mg[0], genres_list[mg[1]]))

    for item in movie_genre_ids:
        writer.writerow([item[0], item[1]])


def write_genres(genre_set, writer):
    sorted_set = sorted(genre_set)
    genres_list = {}
    for idx, genre in enumerate(sorted_set):
        if genre not in ['(no genres listed)']:
            writer.writerow([idx, genre])
            genres_list[genre] = idx
    return genres_list


def write_movie(movie_id, movie_name, movie_year, writer):
    writer.writerow([movie_id.strip(), movie_name.strip(), movie_year.strip()])


def parse_file(genre_set, reader, movies_file, movie_genres_file):
    movies_writer = csv.writer(movies_file, delimiter='#')

    movie_genres_list = []
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            # Create column values
            movie_id = row[0]
            movie_name, movie_year = parse_name_and_year(row[1])
            movie_genres = parse_genres(row[2])

            # Add unique genre names to genre-set
            genre_set = genre_set.union(movie_genres)

            # Append values to movie and movie-genre files
            write_movie(movie_id, movie_name, movie_year, movies_writer)
            movie_genres_list = movie_genres_list + \
                create_movie_genres(movie_id, movie_genres)

        line_count += 1

    return line_count, genre_set, movie_genres_list


def parse_files(read_file, movies_file, genres_file, movie_genres_file):
    reader = csv.reader(read_file, delimiter=',')
    genres_writer = csv.writer(genres_file, delimiter='#')
    movie_genres_writer = csv.writer(movie_genres_file, delimiter='#')

    # Parse file
    genre_set = set({})
    movie_genres_list = []

    print('Parsing movies file...')
    line_count, genre_set, movie_genres_list = parse_file(
        genre_set, reader, movies_file, movie_genres_file)

    # Write set of all the unique genre names
    genres_list = write_genres(genre_set, genres_writer)

    # Write all movie genre id combinations
    write_movie_genres(movie_genres_list, genres_list, movie_genres_writer)
    print('Finished writing genres file...')

    return line_count

# Open 1 read file to parse, and 3 write files which will represent SQL data


def parse_movie_file(input_file, movies_output, genres_output, movie_genres_output):
    with open(input_file) as read_file, \
            open(movies_output, mode='w') as movies_file, \
            open(genres_output, mode='w') as genres_file, \
            open(movie_genres_output, mode='w') as movie_genres_file:

        lines_parsed = parse_files(
            read_file, movies_file, genres_file, movie_genres_file)

        print(f'Processed {lines_parsed} lines in movies file')
