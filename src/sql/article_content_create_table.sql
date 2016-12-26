CREATE TABLE IF NOT EXISTS ako_article_content
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    article INT,
    lang INT,
    title TEXT,
    description TEXT,
    content TEXT,
    CONSTRAINT ako_article_content_ako_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_article_content_ako_lang_fk FOREIGN KEY (lang) REFERENCES ako_lang (id)
);