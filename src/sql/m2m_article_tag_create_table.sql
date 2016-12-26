CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_tag
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    tag INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_tag_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_tag_ako_m2m_article_tag_tag_fk FOREIGN KEY (tag) REFERENCES ako_tag (id)
);