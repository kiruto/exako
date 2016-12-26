CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_image
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    image INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_image_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_image_ako_m2m_article_image_image_fk FOREIGN KEY (image) REFERENCES ako_image (id)
);