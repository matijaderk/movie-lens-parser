import csv


def write_user_ids(users_set, writer):
    users_list = list(users_set)
    sorted_list = sorted(users_list)

    for user_id in sorted_list:
        writer.writerow([user_id])


def parse_file(reader, users_set):
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            users_set.add(int(row[0]))
        line_count += 1

    return line_count


def parse_files(read_tags_file, read_ratings_file, users_file):
    tags_reader = csv.reader(read_tags_file, delimiter=',')
    ratings_reader = csv.reader(read_ratings_file, delimiter=',')
    users_writer = csv.writer(users_file, delimiter='#')

    # Parse file
    users_set = set({})

    print('Parsing tags file...')
    line_count_tags = parse_file(tags_reader, users_set)
    print(f'Processed {line_count_tags} lines in tags file')

    print('Parsing ratings file...')
    line_count_ratings = parse_file(ratings_reader, users_set)
    print(f'Processed {line_count_ratings} lines in ratings file')

    print('Writing to users file...')
    write_user_ids(users_set, users_writer)


def create_user_file(tags_file, ratings_file, users_file_output):
    with open(tags_file) as read_tags_file, \
            open(ratings_file) as read_ratings_file, \
            open(users_file_output, mode='w') as write_users_file:

        lines_parsed = parse_files(
            read_tags_file, read_ratings_file, write_users_file)
