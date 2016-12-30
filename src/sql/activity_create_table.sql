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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE INDEX ako_activity_tag__index ON ako_activity (tag);
CREATE INDEX ako_activity_time__index ON ako_activity (created_at);