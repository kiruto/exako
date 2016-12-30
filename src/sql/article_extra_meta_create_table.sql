CREATE TABLE IF NOT EXISTS ako_article_extra_meta
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE UNIQUE INDEX ako_article_extra_meta_name_uindex ON exako.ako_article_extra_meta (name);