CREATE TABLE IF NOT EXISTS ako_article_extra
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    prop INT NOT NULL,
    val TEXT,
    CONSTRAINT ako_article_extra_ako_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_article_extra_ako_article_extra_meta_fk FOREIGN KEY (prop) REFERENCES ako_article_extra_meta (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8md4;