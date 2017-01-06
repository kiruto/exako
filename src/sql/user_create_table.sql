CREATE TABLE IF NOT EXISTS user
(
    uid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    password CHAR NOT NULL,
    name CHAR NOT NULL,
    mail CHAR,
    extra BLOB
) ENGINE=InnoDB DEFAULT CHARSET=utf8md4;
CREATE UNIQUE INDEX user_name_uindex ON user (name);
CREATE UNIQUE INDEX user_mail_uindex ON user (mail);
ALTER TABLE user COMMENT = 'all user information';