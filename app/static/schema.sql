CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, username TEXT NOT NULL, pwd_hash TEXT NOT NULL);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, category STRING NOT NULL, entry_id STRING REFERENCES entries (id) NOT NULL);
CREATE TABLE entries (id INTEGER CONSTRAINT "UNIQUE" PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, title TEXT, url TEXT, body TEXT, image BLOB, 
datetime STRING NOT NULL, user_id INTEGER NOT NULL, filename STRING, mimetype STRING);