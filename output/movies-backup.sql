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

CREATE TABLE public.genres (
    id integer NOT NULL,
    name text
);

CREATE TABLE public.links (
    "movie-id" integer NOT NULL,
    "imdb-id" text DEFAULT ''::text,
    "tmdb-id" text
);

CREATE TABLE public.movies (
    "movie-id" integer NOT NULL,
    title text,
    year integer
);

CREATE TABLE public."movie-genre" (
    "movie-id" integer,
    "genre-id" integer
);

CREATE TABLE public.ratings (
    "user-id" integer,
    "movie-id" integer,
    rating real,
    "timestamp" text
);

ALTER TABLE public.genres OWNER TO postgres;
ALTER TABLE public.links OWNER TO postgres;
ALTER TABLE public.movies OWNER TO postgres;
ALTER TABLE public."movie-genre" OWNER TO postgres;
ALTER TABLE public.ratings OWNER TO postgres;

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);
ALTER TABLE ONLY public.links
    ADD CONSTRAINT links_pkey PRIMARY KEY ("movie-id");
ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY ("movie-id");

COPY public.genres(id, name) 
FROM '/Path/To/Output/genres.csv' DELIMITER '#' CSV;

COPY public.links("movie-id", "imdb-id", "tmdb-id")
FROM '/Path/To/Output/links.csv' DELIMITER ',' CSV;

COPY public.movies("movie-id", title, year)
FROM '/Path/To/Output/movies.csv' DELIMITER '#' CSV;

copy public."movie-genre"("movie-id", "genre-id")
FROM '/Path/To/Output/movie-genres.csv' DELIMITER '#' CSV;

copy public.ratings("user-id", "movie-id", rating, "timestamp")
FROM '/Path/To/Output/ratings.csv' DELIMITER ',' CSV;
