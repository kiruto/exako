CREATE TABLE IF NOT EXISTS exako.ako_tag_value
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tag INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    lang INT,
    CONSTRAINT ako_tag_ako_tag_value_tag_fk FOREIGN KEY (tag) REFERENCES ako_tag (id),
    CONSTRAINT ako_tag_ako_tag_value_lang_fk FOREIGN KEY (lang) REFERENCES ako_lang(id)
);