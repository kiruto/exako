CREATE TABLE IF NOT EXISTS exako.ako_site_meta
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) UNIQUE NOT NULL,
    comment TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE UNIQUE INDEX ako_site_meta_name_uindex ON exako.ako_site_meta (name);