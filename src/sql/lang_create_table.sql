CREATE TABLE IF NOT EXISTS exako.ako_lang
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) UNIQUE NOT NULL
);
CREATE UNIQUE INDEX ako_lang_name_uindex ON exako.ako_lang (name);