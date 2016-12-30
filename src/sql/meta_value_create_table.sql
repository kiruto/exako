CREATE TABLE IF NOT EXISTS exako.ako_meta_value
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    key_name INT NOT NULL,
    value TEXT,
    lang INT NOT NULL,
    CONSTRAINT ako_site_meta_ako_meta_id_fk FOREIGN KEY (key_name) REFERENCES ako_site_meta (id),
    CONSTRAINT ako_site_meta_ako_lang_id_fk FOREIGN KEY (lang) REFERENCES ako_lang (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE INDEX ako_meta_value_key_name_uindex on exako.ako_meta_value (key_name);
CREATE INDEX ako_meta_value_lang_uindex on exako.ako_meta_value (lang);