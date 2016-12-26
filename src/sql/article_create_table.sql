CREATE TABLE IF NOT EXISTS ako_article
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cat INT,
    created_at TIMESTAMP DEFAULT current_timestamp,
    CONSTRAINT ako_article_ako_tag_fk FOREIGN KEY (cat) REFERENCES ako_tag (id)
);