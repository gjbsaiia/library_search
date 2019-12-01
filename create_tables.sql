
CREATE TABLE Library(
name VARCHAR(20) NOT NULL,
address	 VARCHAR(30),
dateFounded DATE,
UNIQUE (address),
PRIMARY KEY (name)
);

CREATE TABLE Library_Books(
library_name VARCHAR(20) FORIGN KEY REFERENCES Library(name) NOT NULL,
book_ID VARCHAR(30) FORIGN KEY REFERENCES Book(book_ID) NOT NULL,
count	DECIMAL(2,0) NOT NULL CHECK (count >= 0)
PRIMARY KEY(library_name, book_ID)
);

CREATE TABLE Book(
book_ID VARCHAR(30),
title VARCHAR(30),
description TEXT,
genre VARCHAR(18) NOT NULL CHECK (genre IN (‘Non-Fiction’, ‘Children’, ‘Drama’, ‘Fantasy’, ‘Graphic Novel’, ‘Horor’, ‘Mystery’, ‘Poetry’, ‘Romance’, ‘Satire’, ‘Biography’, ‘Auto-Biography’,’Thriller’, ‘Young Adult’, ‘other’)),
publisher_ID VaRCHAR(20) FOREIGN KEY REFERENCES Publisher (publisher_ID) NOT NULL,
date_published DATE,
PRIMARY KEY(book_ID)
);

CREATE TABLE Written_By(
book_ID VARCHAR(30) FOREIGN KEY REFERENCES Book(book_ID) NOT NULL,
author_ID VARCHAR(20) FOREIGN KEY REFERENCES Author(author_ID) NOT NULL,
PRIMARY KEY(book_ID, author_ID)
);

CREATE TABLE User(
user_ID VARCHAR(20) NOT NULL,
name VARCHAR(20) NOT NULL,
PRIMARY KEY(user_ID)
);

CREATE TABLE Checks_Out(
user_ID VARCHAR(20) FOREIGN KEY REFERENCES User(user_ID) NOT NULL,
book_ID VARCHAR(30) FOREIGN KEY REFERENCES Book(book_ID) NOT NULL,
library_name VARCHAR(20) FOREIGN KEY REFERENCES Library(name) NOT NULL,
due DATE,
PRIMARY KEY(user_ID, book_ID, library_name)
);

CREATE TABLE Author(
author_ID VARCHAR(20) NOT NULL,
name VARCHAR(20) NOT NULL,
DOB DATE,
PRIMARY KEY(author_ID)
);

CREATE TABLE Publisher(
publisher_ID VARCHAR(20) NOT NULL,
name VARCHAR(20),
location VARCHAR(20),
PRIMARY KEY(publisher_ID)
);

CREATE TABLE Librarian(
librarian_ID VARCHAR(20) NOT NULL,
name VARCHAR(20),
library_name VARCHAR(20) FOREIGN KEY REFERENCES Library(name) NOT NULL,
PRIMARY KEY(librarian_ID)
);

CREATE TABLE Librarian-Genres(
librarian_ID VARCHAR(20) FOREIGN KEY REFERENCES Librarian(librarian_ID) NOT NULL,
genre VARCHAR(18) NOT NULL CHECK (genre IN (‘Non-Fiction’, ‘Children’, ‘Drama’, ‘Fantasy’, ‘Graphic Novel’, ‘Horor’, ‘Mystery’, ‘Poetry’, ‘Romance’, ‘Satire’, ‘Biography’, ‘Auto-Biography’,’Thriller’, ‘Young Adult’, ‘other’)),
PRIMARY KEY(librarian_ID, genre)
);
