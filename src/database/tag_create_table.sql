CREATE TABLE IF NOT EXISTS ako_tag
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    extra TEXT
);
CREATE UNIQUE INDEX ako_tag_name_uindex ON ako_tag (name);