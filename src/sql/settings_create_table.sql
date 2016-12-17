CREATE TABLE IF NOT EXISTS exako.ako_settings
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    value TEXT,
    comment TEXT
);

CREATE UNIQUE INDEX ako_settings_name_uindex ON exako.ako_settings (name);