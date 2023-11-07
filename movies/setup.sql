-- Create tables
CREATE TABLE movies (
    id INTEGER,
    title TEXT NOT NULL,
    year TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT NOT NULL,
    birth TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE stars (
    movie_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL
);
CREATE TABLE directors (
    movie_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL
);
CREATE TABLE ratings (
    movie_id INTEGER NOT NULL,
    rating REAL NOT NULL,
    votes INTEGER NOT NULL,
    PRIMARY KEY(movie_id)
);

-- Movies and Ratings
INSERT INTO movies (title, year) VALUES ("A Few Good Men", 1992);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "A Few Good Men"), 7.7, 218512);
INSERT INTO movies (title, year) VALUES ("The Shawshank Redemption", 1994);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Shawshank Redemption"), 9.3, 2150648);
INSERT INTO movies (title, year) VALUES ("Toy Story", 1995);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Toy Story"), 8.3, 819238);
INSERT INTO movies (title, year) VALUES ("Apollo 13", 1995);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Apollo 13"), 7.6, 250710);
INSERT INTO movies (title, year) VALUES ("Catch Me If You Can", 2002);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Catch Me If You Can"), 8.1, 741363);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Chamber of Secrets", 2002);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Chamber of Secrets"), 7.4, 504212);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Sorcerer's Stone", 2001);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Sorcerer's Stone"), 7.6, 582405);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Prisoner of Azkaban", 2004);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Prisoner of Azkaban"), 7.9, 500820);
INSERT INTO movies (title, year) VALUES ("The Incredibles", 2004);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Incredibles"), 8.0, 616425);
INSERT INTO movies (title, year) VALUES ("Corpse Bride", 2005);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Corpse Bride"), 7.3, 227219);
INSERT INTO movies (title, year) VALUES ("Charlie and the Chocolate Factory", 2005);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Charlie and the Chocolate Factory"), 6.6, 396753);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Goblet of Fire", 2005);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Goblet of Fire"), 7.7, 499613);
INSERT INTO movies (title, year) VALUES ("The Departed", 2006);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Departed"), 8.5, 1099707);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Order of the Phoenix", 2007);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Order of the Phoenix"), 7.5, 464255);
INSERT INTO movies (title, year) VALUES ("The Dark Knight", 2008);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Dark Knight"), 9.0, 2121210);
INSERT INTO movies (title, year) VALUES ("Iron Man", 2008);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Iron Man"), 7.9, 884358);
INSERT INTO movies (title, year) VALUES ("Slumdog Millionaire", 2008);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Slumdog Millionaire"), 8.0, 757439);
INSERT INTO movies (title, year) VALUES ("Kung Fu Panda", 2008);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Kung Fu Panda"), 7.5, 389857);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Half-Blood Prince", 2009);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Half-Blood Prince"), 7.6, 428590);
INSERT INTO movies (title, year) VALUES ("Alice in Wonderland", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Alice in Wonderland"), 6.4, 363967);
INSERT INTO movies (title, year) VALUES ("The King's Speech", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The King's Speech"), 8.0, 602856);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Deathly Hallows: Part 1", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Deathly Hallows: Part 1"), 7.7, 435733);
INSERT INTO movies (title, year) VALUES ("Shutter Island", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Shuttler Island"), 8.1, 1031803);
INSERT INTO movies (title, year) VALUES ("How to Train Your Dragon", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "How to Train Your Dragon"), 8.1, 623307);
INSERT INTO movies (title, year) VALUES ("Toy Story 3", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Toy Story 3"), 8.3, 704300);
INSERT INTO movies (title, year) VALUES ("Iron Man 2", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Iron Man 2"), 7.0, 674548);
INSERT INTO movies (title, year) VALUES ("Inception", 2010);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Inception"), 8.8, 1885009);
INSERT INTO movies (title, year) VALUES ("Harry Potter and the Deathly Hallows: Part 2", 2011);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter and the Deathly Hallows: Part 2"), 8.1, 705872);
INSERT INTO movies (title, year) VALUES ("X-Men: First Class", 2011);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "X-Men: First Class"), 7.7, 619146);
INSERT INTO movies (title, year) VALUES ("Looper", 2012);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Looper"), 7.4, 507656);
INSERT INTO movies (title, year) VALUES ("Django Unchained", 2012);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Django Unchained"), 8.4, 1244109);
INSERT INTO movies (title, year) VALUES ("Prometheus", 2012);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Prometheus"), 7.0, 545157);
INSERT INTO movies (title, year) VALUES ("The Avengers", 2012);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Avengers"), 8.0, 1203836);
INSERT INTO movies (title, year) VALUES ("Life of Pi", 2012);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Life of Pi"), 7.9, 545552);
INSERT INTO movies (title, year) VALUES ("42", 2013);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "42"), 7.5, 90681);
INSERT INTO movies (title, year) VALUES ("The Wolf of Wall Street", 2013);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Wolf of Wall Street"), 8.2, 1064692);
INSERT INTO movies (title, year) VALUES ("Boyhood", 2014);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Boyhood"), 7.9, 319637);
INSERT INTO movies (title, year) VALUES ("Interstellar", 2014);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Interstellar"), 8.6, 1340748);
INSERT INTO movies (title, year) VALUES ("Ma Rainey's Black Bottom", 2020);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Ma Rainey's Black Bottom"), 6.9, 47141);
INSERT INTO movies (title, year) VALUES ("Get on Up", 2014);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Get on Up"), 6.9, 23959);
INSERT INTO movies (title, year) VALUES ("Draft Day", 2014);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Draft Day"), 6.8, 49763);
INSERT INTO movies (title, year) VALUES ("The Revenant", 2015);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Revenant"), 8.0, 639623);
INSERT INTO movies (title, year) VALUES ("Alice Through the Looking Glass", 2016);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Alice Through the Looking Glass"), 6.2, 82595);
INSERT INTO movies (title, year) VALUES ("Message from the King", 2016);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Message from the King"), 6.4, 10031);
INSERT INTO movies (title, year) VALUES ("Harry Potter: A History of Magic", 2017);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Harry Potter: A History of Magic"), 7.2, 213);
INSERT INTO movies (title, year) VALUES ("Black Panther", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Black Panther"), 7.3, 680937);
INSERT INTO movies (title, year) VALUES ("Marshall", 2017);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Marshall"), 7.3, 23020);
INSERT INTO movies (title, year) VALUES ("Avengers: Infinity War", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Avengers: Infinity War"), 8.5, 718385);
INSERT INTO movies (title, year) VALUES ("Roma", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Roma"), 7.4, 10594);
INSERT INTO movies (title, year) VALUES ("Incredibles 2", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Incredibles 2"), 7.7, 217333);
INSERT INTO movies (title, year) VALUES ("Eighth Grade", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Eighth Grade"), 7.5, 328713);
INSERT INTO movies (title, year) VALUES ("The Professor", 2018);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Professor"), 6.7, 12778);
INSERT INTO movies (title, year) VALUES ("Toy Story 4", 2019);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Toy Story 4"), 8.0, 118112);
INSERT INTO movies (title, year) VALUES ("Gemini Man", 2019);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Gemini Man"), 5.7, 13752);
INSERT INTO movies (title, year) VALUES ("Happy Times", 2019);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Happy Times"), 10.0, 6);
INSERT INTO movies (title, year) VALUES ("Kirklet", 2019);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Kirklet"), 10.0, 555);
INSERT INTO movies (title, year) VALUES ("Silver Linings Playbook", 2011);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Silver Linings Playbook"), 7.7, 707174);
INSERT INTO movies (title, year) VALUES ("Serena", 2014);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Serena"), 5.4, 29064);
INSERT INTO movies (title, year) VALUES ("American Hustle", 2013);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "American Hustle"), 7.2, 478191);
INSERT INTO movies (title, year) VALUES ("Joy", 2015);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "Joy"), 6.6, 137335);
INSERT INTO movies (title, year) VALUES ("The Hangover", 2009);
INSERT INTO ratings (movie_id, rating, votes) VALUES
    ((SELECT id FROM movies WHERE title = "The Hangover"), 7.7, 781300);

-- People
INSERT INTO people (name, birth) VALUES ("Colin Firth", 1960);
INSERT INTO people (name, birth) VALUES ("Don Rickles", 1926);
INSERT INTO people (name, birth) VALUES ("Christopher Nolan", 1970);
INSERT INTO people (name, birth) VALUES ("Bill Paxton", 1955);
INSERT INTO people (name, birth) VALUES ("Brad Bird", 1957);
INSERT INTO people (name, birth) VALUES ("Frank Darabont", 1959);
INSERT INTO people (name, birth) VALUES ("Gary Sinise", 1955);
INSERT INTO people (name, birth) VALUES ("James McAvoy", 1979);
INSERT INTO people (name, birth) VALUES ("Tom Cruise", 1962);
INSERT INTO people (name, birth) VALUES ("Jim Varney", 1949);
INSERT INTO people (name, birth) VALUES ("Emma Watson", 1990);
INSERT INTO people (name, birth) VALUES ("Jennifer Lawrence", 1990);
INSERT INTO people (name, birth) VALUES ("Emma Stone", 1988);
INSERT INTO people (name, birth) VALUES ("Mackenzie Foy", 2000);
INSERT INTO people (name, birth) VALUES ("Anne Hathaway", 1982);
INSERT INTO people (name, birth) VALUES ("Ethan Hawke", 1970);
INSERT INTO people (name, birth) VALUES ("Michael Fassbender", 1977);
INSERT INTO people (name, birth) VALUES ("Tom Hanks", 1956);
INSERT INTO people (name, birth) VALUES ("Helena Bonham Carter", 1966);
INSERT INTO people (name, birth) VALUES ("Yimou Zhang", 1951);
INSERT INTO people (name, birth) VALUES ("Tim Allen", 1953);
INSERT INTO people (name, birth) VALUES ("Jessica Chastain", 1977);
INSERT INTO people (name, birth) VALUES ("Johnny Depp", 1963);
INSERT INTO people (name, birth) VALUES ("Kevin Bacon", 1958);
INSERT INTO people (name, birth) VALUES ("Leonardo DiCaprio", 1974);
INSERT INTO people (name, birth) VALUES ("Matthew McConaughey", 1969);
INSERT INTO people (name, birth) VALUES ("Ellar Coltrane", 1994);
INSERT INTO people (name, birth) VALUES ("Patricia Arquette", 1968);
INSERT INTO people (name, birth) VALUES ("Chadwick Boseman", 1977);
INSERT INTO people (name, birth) VALUES ("Samuel L. Jackson", 1948);
INSERT INTO people (name, birth) VALUES ("Holly Hunter", 1958);
INSERT INTO people (name, birth) VALUES ("Jason Lee", 1970);
INSERT INTO people (name, birth) VALUES ("Craig T. Nelson", 1944);
INSERT INTO people (name, birth) VALUES ("Richard Griffifths", 1947);
INSERT INTO people (name, birth) VALUES ("Rupert Grint", 1988);
INSERT INTO people (name, birth) VALUES ("Daniel Radcliffe", 1989);
INSERT INTO people (name, birth) VALUES ("Bradley Cooper", 1975);

-- Stars
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Tom Hanks"),
    (SELECT id FROM movies WHERE title = "Toy Story"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Tim Allen"),
    (SELECT id FROM movies WHERE title = "Toy Story"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Don Rickles"),
    (SELECT id FROM movies WHERE title = "Toy Story"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jim Varney"),
    (SELECT id FROM movies WHERE title = "Toy Story"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Ellar Coltrane"),
    (SELECT id FROM movies WHERE title = "Boyhood"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Patricia Arquette"),
    (SELECT id FROM movies WHERE title = "Boyhood"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Ethan Hawke"),
    (SELECT id FROM movies WHERE title = "Boyhood"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Matthew McConaughey"),
    (SELECT id FROM movies WHERE title = "Interstellar"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Anne Hathaway"),
    (SELECT id FROM movies WHERE title = "Interstellar"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jessica Chastain"),
    (SELECT id FROM movies WHERE title = "Interstellar"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Mackenzie Foy"),
    (SELECT id FROM movies WHERE title = "Interstellar"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "Inception"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "The Departed"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "Django Unchained"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "The Wolf of Wall Street"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "Catch Me If You Can"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Leonardo DiCaprio"),
    (SELECT id FROM movies WHERE title = "The Revenant"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Johnny Depp"),
    (SELECT id FROM movies WHERE title = "Corpse Bride"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Helena Bonham Carter"),
    (SELECT id FROM movies WHERE title = "Corpse Bride"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Johnny Depp"),
    (SELECT id FROM movies WHERE title = "Charlie and the Chocolate Factory"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Helena Bonham Carter"),
    (SELECT id FROM movies WHERE title = "Charlie and the Chocolate Factory"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Johnny Depp"),
    (SELECT id FROM movies WHERE title = "Alice in Wonderland"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Helena Bonham Carter"),
    (SELECT id FROM movies WHERE title = "Alice in Wonderland"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Johnny Depp"),
    (SELECT id FROM movies WHERE title = "Alice Through the Looking Glass"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Helena Bonham Carter"),
    (SELECT id FROM movies WHERE title = "Alice Through the Looking Glass"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Johnny Depp"),
    (SELECT id FROM movies WHERE title = "The Professor"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Helena Bonham Carter"),
    (SELECT id FROM movies WHERE title = "The King's Speech"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Colin Firth"),
    (SELECT id FROM movies WHERE title = "The King's Speech"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Kevin Bacon"),
    (SELECT id FROM movies WHERE title = "X-Men: First Class"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Kevin Bacon"),
    (SELECT id FROM movies WHERE title = "Apollo 13"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Kevin Bacon"),
    (SELECT id FROM movies WHERE title = "A Few Good Men"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "James McAvoy"),
    (SELECT id FROM movies WHERE title = "X-Men: First Class"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Michael Fassbender"),
    (SELECT id FROM movies WHERE title = "X-Men: First Class"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jennifer Lawrence"),
    (SELECT id FROM movies WHERE title = "X-Men: First Class"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Tom Hanks"),
    (SELECT id FROM movies WHERE title = "Apollo 13"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bill Paxton"),
    (SELECT id FROM movies WHERE title = "Apollo 13"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Gary Sinise"),
    (SELECT id FROM movies WHERE title = "Apollo 13"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Tom Cruise"),
    (SELECT id FROM movies WHERE title = "A Few Good Men"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "42"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Black Panther"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Marshall"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Ma Rainey's Black Bottom"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Get on Up"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Draft Day"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Chadwick Boseman"),
    (SELECT id FROM movies WHERE title = "Message from the King"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Samuel L. Jackson"),
    (SELECT id FROM movies WHERE title = "The Incredibles"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Holly Hunter"),
    (SELECT id FROM movies WHERE title = "The Incredibles"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jason Lee"),
    (SELECT id FROM movies WHERE title = "The Incredibles"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Craig T. Nelson"),
    (SELECT id FROM movies WHERE title = "The Incredibles"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Richard Griffifths"),
    (SELECT id FROM movies WHERE title = "Harry Potter and the Prisoner of Azkaban"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Rupert Grint"),
    (SELECT id FROM movies WHERE title = "Harry Potter and the Prisoner of Azkaban"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Daniel Radcliffe"),
    (SELECT id FROM movies WHERE title = "Harry Potter and the Prisoner of Azkaban"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Emma Watson"),
    (SELECT id FROM movies WHERE title = "Harry Potter and the Prisoner of Azkaban"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bradley Cooper"),
    (SELECT id FROM movies WHERE title = "Silver Linings Playbook"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bradley Cooper"),
    (SELECT id FROM movies WHERE title = "Serena"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bradley Cooper"),
    (SELECT id FROM movies WHERE title = "American Hustle"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bradley Cooper"),
    (SELECT id FROM movies WHERE title = "Joy"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jennifer Lawrence"),
    (SELECT id FROM movies WHERE title = "Silver Linings Playbook"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jennifer Lawrence"),
    (SELECT id FROM movies WHERE title = "Serena"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jennifer Lawrence"),
    (SELECT id FROM movies WHERE title = "American Hustle"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Jennifer Lawrence"),
    (SELECT id FROM movies WHERE title = "Joy"));
INSERT INTO stars (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Bradley Cooper"),
    (SELECT id FROM movies WHERE title = "The Hangover"));

-- Directors
INSERT INTO directors (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Christopher Nolan"),
    (SELECT id FROM movies WHERE title = "The Dark Knight"));
INSERT INTO directors (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Yimou Zhang"),
    (SELECT id FROM movies WHERE title = "Happy Times"));
INSERT INTO directors (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Brad Bird"),
    (SELECT id FROM movies WHERE title = "Incredibles 2"));
INSERT INTO directors (person_id, movie_id) VALUES (
    (SELECT id FROM people WHERE name = "Frank Darabont"),
    (SELECT id FROM movies WHERE title = "The Shawshank Redemption"));
