CREATE TABLE IF NOT EXISTS exako.ako_site_meta
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    value TEXT,
    lang INT NOT NULL,
    CONSTRAINT ako_site_meta_ako_lang_id_fk FOREIGN KEY (lang) REFERENCES ako_lang (id)
);
CREATE INDEX ako_site_meta_key_uindex ON exako.ako_site_meta (name);
CREATE INDEX ako_meta_lang__index ON exako.ako_site_meta (lang);