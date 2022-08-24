-- создадим необходимые таблицы
create table if not exists hw.movies(
id serial primary key,
title VARCHAR(255),
year integer
);
create table if not exists hw.actors(
id serial primary key,
	name TEXT
);
create table if not exists hw.directors(
id serial primary key,
	name TEXT,
	born integer
);

create table if not exists hw.created(
id serial primary key,
	director_id bigint REFERENCES hw.directors(id),
	movie_id bigint references hw.movies(id)
);

create table if not exists hw.played_in(
id serial primary key,
	movie_id bigint references hw.movies(id),
	actor_id bigint references hw.actors(id),
	character text
);

-- добавим режиссёров
insert into hw.directors(name) values ('Joel Coen');
insert into hw.directors(name, born) values ('Ethan Coen', 1957);
insert into hw.directors(name) values ('Martin McDonagh');
insert into hw.directors(name) values ('Christopher Nolan');
insert into hw.directors(name) values ('Ruben Fleischer');

-- добавим фильмы
insert into hw.movies(title, year) values('Blood Simple', 1983);
insert into hw.movies(title) values('Three Billboards Outside Ebbing, Missouri');
insert into hw.movies(title) values('Venom');
insert into hw.movies(title) values('Inception');
insert into hw.movies(title) values('The Dark Knight Rises');

-- добавим актёров
insert into hw.actors(name) values('Frances McDormand');
insert into hw.actors(name) values('Woody Harrelson');
insert into hw.actors(name) values('Tom Hardy');
insert into hw.actors(name) values('Marion Cotillard');
insert into hw.actors(name) values('Leonardo DiCaprio');

-- добавим информацию в created
insert into hw.created(director_id,movie_id) values (1,1)
insert into hw.created(director_id,movie_id) values (3,2)
insert into hw.created(director_id,movie_id) values (5,3)
insert into hw.created(director_id,movie_id) values (4,4)
insert into hw.created(director_id,movie_id) values (4,5)

-- добавляем информацию в played_in
insert into hw.played_in(movie_id, actor_id, character) values(1, 1, 'Abby')
insert into hw.played_in(movie_id, actor_id) values(2, 1)
insert into hw.played_in(movie_id, actor_id) values(2, 2)
insert into hw.played_in(movie_id, actor_id) values(3, 2)
insert into hw.played_in(movie_id, actor_id) values(3, 3)
insert into hw.played_in(movie_id, actor_id) values(3, 4)