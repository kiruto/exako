CREATE TABLE IF NOT EXISTS ako_activity
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    platform VARCHAR(255),
    source_url TEXT,
    created_at TIMESTAMP DEFAULT current_timestamp,
    title TEXT,
    description TEXT,
    thumbnail_url TEXT,
    tag VARCHAR(255) DEFAULT '[]',
    extra TEXT
);
CREATE INDEX ako_activity_tag__index ON ako_activity (tag);
CREATE INDEX ako_activity_time__index ON ako_activity (created_at);

CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_image
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    image INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_image_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_image_ako_m2m_article_image_image_fk FOREIGN KEY (image) REFERENCES ako_image (id)
);

CREATE TABLE IF NOT EXISTS exako.ako_m2m_article_tag
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    article INT NOT NULL,
    tag INT NOT NULL,
    CONSTRAINT ako_article_ako_m2m_article_tag_article_fk FOREIGN KEY (article) REFERENCES ako_article (id),
    CONSTRAINT ako_tag_ako_m2m_article_tag_tag_fk FOREIGN KEY (tag) REFERENCES ako_tag (id)
);