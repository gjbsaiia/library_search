BEGIN;
--
-- Create model Author
--
CREATE TABLE `searchsite_author` (`author_ID` varchar(20) NOT NULL PRIMARY KEY, `name` varchar(20) NOT NULL, `DOB` date NULL);
--
-- Create model Library
--
CREATE TABLE `searchsite_library` (`name` varchar(20) NOT NULL PRIMARY KEY, `address` varchar(30) NOT NULL UNIQUE, `dateFounded` date NULL);
--
-- Create model Publisher
--
CREATE TABLE `searchsite_publisher` (`publisher_ID` varchar(20) NOT NULL PRIMARY KEY, `name` varchar(20) NOT NULL, `location` varchar(20) NULL);
--
-- Create model User
--
CREATE TABLE `searchsite_user` (`user_ID` varchar(20) NOT NULL PRIMARY KEY, `name` varchar(20) NOT NULL);
--
-- Create model Librarian
--
CREATE TABLE `searchsite_librarian` (`librarian_ID` varchar(20) NOT NULL PRIMARY KEY, `name` varchar(20) NOT NULL, `library_name_id` varchar(20) NOT NULL);
--
-- Create model Book
--
CREATE TABLE `searchsite_book` (`book_ID` varchar(30) NOT NULL PRIMARY KEY, `title` varchar(30) NOT NULL, `description` varchar(255) NULL, `genre` varchar(18) NOT NULL, `datePublished` date NULL, `publisher_ID_id` varchar(20) NOT NULL);
--
-- Create model Written_By
--
CREATE TABLE `searchsite_written_by` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `author_ID_id` varchar(20) NOT NULL, `book_ID_id` varchar(30) NOT NULL);
--
-- Create model Library_Books
--
CREATE TABLE `searchsite_library_books` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `count` double precision NOT NULL, `book_ID_id` varchar(30) NOT NULL, `library_name_id` varchar(20) NOT NULL);
--
-- Create model Librarian_Genre
--
CREATE TABLE `searchsite_librarian_genre` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `genre` varchar(18) NOT NULL, `librarian_ID_id` varchar(20) NOT NULL);
--
-- Create model Checks_Out
--
CREATE TABLE `searchsite_checks_out` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `due` date NOT NULL, `book_ID_id` varchar(30) NOT NULL, `library_name_id` varchar(20) NOT NULL, `user_ID_id` varchar(20) NOT NULL);
ALTER TABLE `searchsite_librarian` ADD CONSTRAINT `searchsite_librarian_library_name_id_f73be6ee_fk_searchsit` FOREIGN KEY (`library_name_id`) REFERENCES `searchsite_library` (`name`);
ALTER TABLE `searchsite_book` ADD CONSTRAINT `searchsite_book_publisher_ID_id_009f85f3_fk_searchsit` FOREIGN KEY (`publisher_ID_id`) REFERENCES `searchsite_publisher` (`publisher_ID`);
ALTER TABLE `searchsite_written_by` ADD CONSTRAINT `searchsite_written_b_author_ID_id_d6e7dda1_fk_searchsit` FOREIGN KEY (`author_ID_id`) REFERENCES `searchsite_author` (`author_ID`);
ALTER TABLE `searchsite_written_by` ADD CONSTRAINT `searchsite_written_b_book_ID_id_3bd9cb64_fk_searchsit` FOREIGN KEY (`book_ID_id`) REFERENCES `searchsite_book` (`book_ID`);
ALTER TABLE `searchsite_written_by` ADD CONSTRAINT `searchsite_written_by_book_ID_id_author_ID_id_168490d3_uniq` UNIQUE (`book_ID_id`, `author_ID_id`);
ALTER TABLE `searchsite_library_books` ADD CONSTRAINT `searchsite_library_b_book_ID_id_cab6a427_fk_searchsit` FOREIGN KEY (`book_ID_id`) REFERENCES `searchsite_book` (`book_ID`);
ALTER TABLE `searchsite_library_books` ADD CONSTRAINT `searchsite_library_b_library_name_id_1132d10c_fk_searchsit` FOREIGN KEY (`library_name_id`) REFERENCES `searchsite_library` (`name`);
ALTER TABLE `searchsite_library_books` ADD CONSTRAINT `searchsite_library_books_library_name_id_book_ID__96b3da44_uniq` UNIQUE (`library_name_id`, `book_ID_id`);
ALTER TABLE `searchsite_librarian_genre` ADD CONSTRAINT `searchsite_librarian_librarian_ID_id_1633e6ef_fk_searchsit` FOREIGN KEY (`librarian_ID_id`) REFERENCES `searchsite_librarian` (`librarian_ID`);
ALTER TABLE `searchsite_librarian_genre` ADD CONSTRAINT `searchsite_librarian_genre_librarian_ID_id_genre_883bf7b1_uniq` UNIQUE (`librarian_ID_id`, `genre`);
ALTER TABLE `searchsite_checks_out` ADD CONSTRAINT `searchsite_checks_ou_book_ID_id_5057dae3_fk_searchsit` FOREIGN KEY (`book_ID_id`) REFERENCES `searchsite_book` (`book_ID`);
ALTER TABLE `searchsite_checks_out` ADD CONSTRAINT `searchsite_checks_ou_library_name_id_75e76c82_fk_searchsit` FOREIGN KEY (`library_name_id`) REFERENCES `searchsite_library` (`name`);
ALTER TABLE `searchsite_checks_out` ADD CONSTRAINT `searchsite_checks_ou_user_ID_id_8be80c3b_fk_searchsit` FOREIGN KEY (`user_ID_id`) REFERENCES `searchsite_user` (`user_ID`);
ALTER TABLE `searchsite_checks_out` ADD CONSTRAINT `searchsite_checks_out_user_ID_id_book_ID_id_li_494ddce7_uniq` UNIQUE (`user_ID_id`, `book_ID_id`, `library_name_id`);
COMMIT;
