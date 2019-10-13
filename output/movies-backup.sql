SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;
SET default_tablespace = '';
SET default_with_oids = false;

DROP TABLE IF EXISTS public.genres;
CREATE TABLE public.genres (
  id integer NOT NULL,
  name varchar(255),
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.links;
CREATE TABLE public.links (
  id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
  movie_id integer NOT NULL,
  imdb_id text DEFAULT ''::text,
  tmdb_id text,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.movies;
CREATE TABLE public.movies (
  id integer NOT NULL,
  title varchar(255),
  release_date integer,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.movies_genres;
CREATE TABLE public.movies_genres (
  id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
  movie_id integer,
  genre_id integer,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.ratings;
CREATE TABLE public.ratings (
  id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
  user_id integer,
  movie_id integer,
  rating real,
  rated_at int,
  PRIMARY KEY (id)
);

ALTER TABLE public.genres OWNER TO postgres;
ALTER TABLE public.links OWNER TO postgres;
ALTER TABLE public.movies OWNER TO postgres;
ALTER TABLE public.movies_genres OWNER TO postgres;
ALTER TABLE public.ratings OWNER TO postgres;

COPY public.genres(
  id,
  name
) 
FROM '/Users/mat/Developer/movie-lens-parser/output/genres.csv' DELIMITER '#' CSV;

COPY public.links(
  movie_id,
  imdb_id,
  tmdb_id
)
FROM '/Users/mat/Developer/movie-lens-parser/output/links.csv' DELIMITER ',' CSV;

COPY public.movies(
  id,
  title,
  release_date
)
FROM '/Users/mat/Developer/movie-lens-parser/output/movies.csv' DELIMITER '#' CSV;

copy public.movies_genres(
  movie_id,
  genre_id
)
FROM '/Users/mat/Developer/movie-lens-parser/output/movie-genres.csv' DELIMITER '#' CSV;

copy public.ratings(
  user_id,
  movie_id,
  rating,
  rated_at
)
FROM '/Users/mat/Developer/movie-lens-parser/output/ratings.csv' DELIMITER ',' CSV;
