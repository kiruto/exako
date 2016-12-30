CREATE TABLE IF NOT EXISTS ako_article
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cat INT,
    created_at TIMESTAMP DEFAULT current_timestamp,
    CONSTRAINT ako_article_ako_tag_fk FOREIGN KEY (cat) REFERENCES ako_tag (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_image
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    image INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_image_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_image_ako_m2m_article_image_image_fk FOREIGN KEY (image) REFERENCES ako_image (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_tag
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    tag INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_tag_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_tag_ako_m2m_article_tag_tag_fk FOREIGN KEY (tag) REFERENCES ako_tag (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;