CREATE TABLE exako.ako_site_meta
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    value TEXT,
    lang VARCHAR(20) NOT NULL
);
CREATE UNIQUE INDEX ako_site_meta_key_uindex ON exako.ako_site_meta (name);
CREATE INDEX ako_meta_lang__index ON ako_meta (lang);