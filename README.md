# movie-lens-parser

A small parser for movie recommendation files from MovieLens project (https://grouplens.org/datasets/movielens/).

Creates SQL friendly files which are easily imported into relational database, with clear separation between entities.

# Using parser:

*  Download MovieLens project files from the link above.
*  Place downloaded `.csv` files into input folder.

*  Run `parser.py`, which will create relational .csv files which can then be imported into database.

For example you can import these files into PostgreSQL database like this:
```
COPY movie(id, name, year)
FROM '/output/movies.csv' DELIMITER ','
```