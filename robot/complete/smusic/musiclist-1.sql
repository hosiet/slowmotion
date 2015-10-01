PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE musicdata (
id INTEGER PRIMARY KEY,
filename TEXT NOT NULL,
havenote INTEGER NOT NULL);
INSERT INTO "musicdata" VALUES(1,'年轻的战场.mp3',0);
INSERT INTO "musicdata" VALUES(2,'光荣啊中国共青团(young).mp3',0);
INSERT INTO "musicdata" VALUES(3,'光荣啊,中国共青团.mp3',0);
INSERT INTO "musicdata" VALUES(4,'困兽之斗.mp3',0);
INSERT INTO "musicdata" VALUES(5,'节奏1.mp3',0);
INSERT INTO "musicdata" VALUES(6,'节奏2.mp3',0);
INSERT INTO "musicdata" VALUES(7,'节奏3.mp3',0);
INSERT INTO "musicdata" VALUES(8,'节奏4.mp3',0);
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
time TEXT,
note TEXT);
INSERT INTO "music" VALUES(1,'star','1 1.7 2.4 3.1 3.8 4.5 5.2 6.6 7.3 8 8.7 9.4 10.1 10.8 12.2 12.9 13.6 14.3 15 15.7 16.4 17.8 18.5 19.2 19.9 20.6 21.3 22 23.4 24.1 24.8 25.5 26.2 26.9 27.6 29 29.7 30.4 31.1 31.8 32.5 33.2','1 1 5 5 6 6 5 4 4 3 3 2 2 1 5 5 4 4 3 3 2 5 5 4 4 3 3 2 1 1 5 5 6 6 5 4 4 3 3 2 2 1');
COMMIT;
