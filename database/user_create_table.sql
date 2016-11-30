CREATE TABLE IF NOT EXISTS user
(
    uid INT PRIMARY KEY AUTO_INCREMENT,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    password CHAR NOT NULL,
    name CHAR NOT NULL,
    mail CHAR,
    extra BLOB
);
CREATE UNIQUE INDEX user_name_uindex ON user (name);
CREATE UNIQUE INDEX user_mail_uindex ON user (mail);
ALTER TABLE user COMMENT = 'all user information';