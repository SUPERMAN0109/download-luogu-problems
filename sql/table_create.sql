DROP DATABASE IF EXISTS luogu_problems;
CREATE DATABASE luogu_problems;
USE luogu_problems;
CREATE TABLE tags
(
    id   INT PRIMARY KEY,
    name CHAR(30)
);
CREATE TABLE problems
(
    numb       CHAR(40) PRIMARY KEY,
    name       TINYTEXT NOT NULL,
    difficulty CHAR(20) NOT NULL
);
CREATE TABLE tags_problems_link
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    problem_title CHAR(40),
    tag_id        INT,
    FOREIGN KEY (problem_title) REFERENCES problems (numb),
    FOREIGN KEY (tag_id) REFERENCES tags (id)
);