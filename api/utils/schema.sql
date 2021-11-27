DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT,
  is_verified BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE posts (
  pid INTEGER PRIMARY KEY AUTO_INCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES users (id)
);

insert into users values(username, email, password, is_verified) ('user1' , 'user1@example.com' , 'pbkdf2:sha256:260000$br82oxeDep1o4Svb$03094151072d28b757194a884921d13e7bbffc6794c217bd3fe5538f3e08d814' , 0);