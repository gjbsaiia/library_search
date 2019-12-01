INSERT INTO Library(name, address, dateFounded)
VALUES (‘KSL’, ‘11130 Magnolia Drive’, '1999-7-04');

INSERT INTO Library_Books(book ID, library_name, count)
VALUES (‘BOOK123AB’, ‘KSL’, 3);

INSERT INTO Book(book ID, title, description, genre, publisher_ID, date_published)
VALUES (‘BOOK123AB’, ‘Scarlet Letter’, ‘A woman who gets bullied’, ‘Drama’ ‘PUBL123AB’, ‘1956-8-12’);

INSERT INTO WrittenBy(book ID, author ID)
VALUES (‘BOOK123AB’, ‘AUTH123AB’);

INSERT INTO User(User ID, name)
VALUES (‘USER123AB’, ‘Chris’)

INSERT INTO Check_Out(user ID, book_ID, libray_name, due)
VALUES (‘USER123AB’, ‘BOOK123AB’, ‘ksl’, ‘2019-12-26’);

INSERT INTO Author(author ID, name, DOB)
VALUES (‘AUTH123AB’, ‘Mason Orwell’, ‘1920-8-8’);

INSERT INTO Publisher(publisher ID, name, location)
VALUES
(‘PUBL123AB’, ‘Penguin’, ‘Hollywood Hills’);

INSERT INTO Librarian(librarian ID, name, library_name)
VALUES (‘LIBR123AB’, ‘Jennifer’, ‘KSL’);

INSERT INTO Librarian_Genres(librarian ID, genre)
VALUES (‘LIBR123AB’, ‘Satire’);

Library
INSERT INTO Library VALUES(‘name’,’ address’, ‘dateFounded’)
‘KSL’, ‘11130 Magnolia Drive’, '1999-07-04'
‘HMC’, ‘2160 Adelbert Drive’, ‘1899-02-05’
‘WHT’, ‘230 MLK Road’, ‘1935-04-12’

Library_Books
INSERT INTO Library_Books VALUES(‘book ID’,’ library_name’, ‘count’)
‘BOOK111AB’, ‘KSL’, 3
‘BOOK112DC’, ‘HMC’, 1
‘BOOK113AC’, ‘WHT’, 2
‘BOOK114DD’, ‘WHT’, 5
‘BOOK116DF’, ‘WHT’, 1
‘BOOK117DE’, ‘KSL’, 2
‘BOOK118AC’, ‘HMC’, 1
‘BOOK119VC’, ‘KSL’, 1
‘BOOK120SF’, ‘HMC’, 1
‘BOOK121QF’, ‘HMC’, 1
‘BOOK122ZC’, ‘WHT’, 1
‘BOOK123GH’, ‘KSL’, 5
‘BOOK124DC’, ‘HMC’, 2
‘BOOK125BB’, ‘WHT’, 1
‘BOOK126ZZ’,  ‘KSL’, 1


Book
INSERT INTO Book VALUES (‘book ID’, ‘title’, ‘description’, ‘genre’, ‘publisher_ID’, ‘date_published’)
‘BOOK111AB’, ‘Scarlet Letter’, ‘A woman who gets bullied’, ‘Drama’ ‘PUBL123AB’, ‘1956-09-16’

‘BOOK112DC’, ‘Charlie and the Chocolate Bar’, ‘A boy gets lucky, and his grandad lies about a being bed ridden’, ‘Children’, ‘PUBL112AF’, ‘1923-08-06’

‘BOOK113AC’, ‘White Rabbit’, ‘A bunny finds out people eat them’,’Horror’, ‘PUBL112AF’, ‘1999-02-07’

‘BOOK114DD’, ‘Snoop Dog’, ‘The Complete story of Snoop Dog’, ‘PUBL113AC’, ‘2016-04-05’

‘BOOK116DF’, ‘Harry and The Cup of Warm Water’, ‘A boy finds out he can do magic tricks and enter into a competition with a big reward’, Graphic Novel, ‘PUBL112AF’

‘BOOK117DE’, ‘Good Signs’, ‘The End of the World With a Comedic Twist’, ‘Satire’, ‘PUBL111AB’, ‘1970-02-09’

‘BOOK118AC’, ‘Catch 23’, ‘A sequel to the best seller Catch 22’, ‘Satire’, ‘PUBL114EF’, ‘1919-11-01’

‘BOOK119VC’, ‘Microeconomics for Dummies’, NULL, ‘Non-Fiction’, ‘PUBL113AC’, ‘1923-08-06’

‘BOOK120SF’, ‘Who Framed Rodger Rabbit’, ‘A man tries to blame a rabbit for his failed marriage’, ‘Romance’, ‘PUBL114EF’, ‘1921-02-03’

‘BOOK121QF’, ‘The Alienish’, ‘A murder has been commited, but the only witness is deaf and blind’, ‘Mystery’, ‘PUBL115DE’, ‘1899-02-11’

‘BOOK122ZC’, ‘Blue Waves’, ‘The ocean is my oyster, but the sun is my clam’, ‘Poetry’, ‘PUBL112AF’, ‘1983-01-06’

‘BOOK123GH’, ‘Who is Gahndi’, ‘A good man’, ‘Auto-Biograghy’, ‘PUBL113AC’, ‘1935-08-02’

‘BOOK124DC’, ‘Thriller’, ‘A thrilling book’, ‘Thriller’, ‘PUBL111AB’, ‘1974-01-01’

‘BOOK125BB’, ‘Twilight 2: Electric Boogaloo’, ‘What happens when a Vampire Bites a Werewolf? What happens next will shock you’, ‘Young Adult’, ‘PUBL112AF’, ‘2018-03-03’

‘BOOK126ZZ’, ‘The Moon landing was a hoax’, "How do you go to the moon? The answer is you don't", ‘other’, ‘PUBL111AB’, ‘1996-03-04’

INSERT INTO WrittenBy VALUES (‘book ID’, ‘author ID’)
‘BOOK111AB’, ‘AUTH111AB’
‘BOOK111AB’, ‘AUTH211CD’
‘BOOK112DC’, ‘AUTH211CD’
‘BOOK113AC’, ‘AUTH311CA’
‘BOOK114DD’, ‘AUTH411DD’
‘BOOK116DF’, ‘AUTH611FD’
‘BOOK117DE’, ‘AUTH711ED’
‘BOOK118AC’, ‘AUTH811CA’
‘BOOK119VC’, ‘AUTH912CV’
‘BOOK120SF’, ‘AUTH311CA’
‘BOOK121QF’, ‘AUTH121FQ’
‘BOOK122ZC’, ‘AUTH221CZ’
‘BOOK123GH’, ‘AUTH321HG’
‘BOOK124DC’, ‘AUTH421CD’
‘BOOK125BB’, ‘AUTH411DD’
‘BOOK126ZZ’, ‘AUTH621ZZ’

User
INSERT INTO User VALUES (‘User ID’, ‘name’)
‘USER123AB’, ‘Chris’
‘USER422AC’, ‘Ben’
‘USER423QB’, ‘Emily’
‘USER244AF’, ‘Andrea’
‘USER589AR’, ‘Jack’

Check_Out
INSERT INTO Check_Out VALUES (‘User ID’, ‘book ID’,’library_name’, ‘due’)
‘USER123AB’, ‘BOOK111AB’,’KSL’ ‘2019-12-16’
‘USER422AC’, ‘BOOK123GH’, ‘HMC’, ‘2020-02-02
‘USER423QB’, ‘BOOK126ZZ’, ‘KSL’, ‘2020-04-11’
‘USER589AR’, ‘BOOK114DD’, ‘WHT’, ‘2020-01-03’
‘USER244AF’, ‘BOOK114DD’, ‘WHT’, ‘2020-01-09’

Author
INSERT INTO Author VALUES(‘author ID’, ‘name, DOB’)
‘AUTH111AB’, ‘Mason Orwell’, ‘1920-08-08’
‘AUTH211CD’, ‘Clark Kent’, ‘1878-03-04’
‘AUTH311CA’, ‘Bruce Wyane’, ‘1970-04-02’
‘AUTH411DD’, ‘Peter Parker’, ‘1990-03-01’
‘AUTH611FD’, ‘Bruce Banner’, ‘1986-02-04’
‘AUTH711ED’, ‘Dr. Strange’, ‘1940-03-09’
‘AUTH811CA’, ‘Captain America’, ‘1880-05-02’
‘AUTH912CV’, ‘Luis Lane’, ‘1895-03-04’
‘AUTH121FQ’, ‘Oliver Queen’, ‘1859-07-07’
‘AUTH221CZ’, ‘Logan’, ‘1957-03-05’
‘AUTH321HG’, ‘Ghandi’, ‘1869-07-02’
‘AUTH421CD’, ‘Specer Spencer’, ‘1943-09-09’
‘AUTH621ZZ’, ‘Scott Summers’, ‘1962-06-02’

Publisher
INSERT INTO Publisher VALUES(‘publisher ID’, ‘name’, ‘location’)
‘PUBL111AB’, ‘Penguin’, ‘Hollywood Hills’
‘PUBL112AF’, ‘Goose’, ‘Brooklyn’
‘PUBL114EF’, ‘Panther’, ‘Queens’
‘PUBL113AC’, Hamster’, ‘Chicago’
‘PUBL115DE’, ‘JackRabbit’, ‘Philadelphia’

Librarian
INSERT INTO Librarian VALUES(‘librarian ID’, ‘name’, ‘library_name’)
‘LIBR110AF’, ‘Jennifer’, ‘KSL’
‘LIBR120WF’, ‘Candice’, ‘KSL’
‘LIBR130TP’, ‘Alex’, ‘WHT’
‘LIBR140HF’, ‘Jerry’, ‘WHT’
‘LIBR150LJ’, ‘Juliette’, ‘HMC’

Librarian_Genres
INSERT INTO Librarian_Genres VALUES(‘librarian ID’, ‘genre’)
‘LIBR110AF’, ‘Horror’
‘LIBR110AF’, ‘Non-Fiction’
‘LIBR110AF’, ‘Mystery’
‘LIBR120WF’, ‘Poetry’
‘LIBR120WF’, ‘Romance
‘LIBR130TP’, ‘Non-Fiction’
‘LIBR130TP’, ‘other’
‘LIBR140HF’, ‘Satire’
‘LIBR150LJ’, ‘Young Adult’
‘LIBR150LJ’, ‘Auto-Biography’
‘LIBR150LJ’,’Children’
