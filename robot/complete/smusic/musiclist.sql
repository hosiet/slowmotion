PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
DROP TABLE musicdata;
DROP TABLE music;
CREATE TABLE musicdata (
id INTEGER PRIMARY KEY,
filename TEXT NOT NULL,
havenote INTEGER NOT NULL);
INSERT INTO "musicdata" VALUES(null,'年轻的战场',0);
--INSERT INTO "musicdata" VALUES(null,'光荣啊中国共青团(young).mp3',0);
INSERT INTO "musicdata" VALUES(null,'光荣啊中国共青团',0);
INSERT INTO "musicdata" VALUES(null,'困兽之斗',0);
INSERT INTO "musicdata" VALUES(null,'最炫民族风',0);
INSERT INTO "musicdata" VALUES(null,'青春修炼手册',0);
INSERT INTO "musicdata" VALUES(null,'节奏一',0);
INSERT INTO "musicdata" VALUES(null,'节奏二',0);
INSERT INTO "musicdata" VALUES(null,'节奏三',0);
INSERT INTO "musicdata" VALUES(null,'节奏四',0);
INSERT INTO "musicdata" VALUES(null,'startup',0);
INSERT INTO "musicdata" VALUES(null,'startup',0);
CREATE TABLE music (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
time TEXT,
note TEXT);
INSERT INTO "music" VALUES(null,'小星星','1 1.7 2.4 3.1 3.8 4.5 5.2 6.6 7.3 8 8.7 9.4 10.1 10.8 12.2 12.9 13.6 14.3 15 15.7 16.4 17.8 18.5 19.2 19.9 20.6 21.3 22 23.4 24.1 24.8 25.5 26.2 26.9 27.6 29 29.7 30.4 31.1 31.8 32.5 33.2','1 1 5 5 6 6 5 4 4 3 3 2 2 1 5 5 4 4 3 3 2 5 5 4 4 3 3 2 1 1 5 5 6 6 5 4 4 3 3 2 2 1');
INSERT INTO "music" VALUES(null,'团歌', '0.5 0.9 1.2 1.5 1.8 2.1 2.9 3.2 3.6 3.9', '0 - = = = = 0 - 0 6');
INSERT INTO "music" VALUES(null,'音乐一','1 1.5 2 3 3.5 4 5 5.5 6 6.5 7 7.5 8 9 9.5 10 11 11.5 12 13 13.5 14 14.5 15 16.5 17 17.5 18 18.5 19 19.5 20.5 21 21.5 22 22.5 23 23.5 24.5 25 25.5 26.5 27 27.5 28.5 29 29.5 30 30.5','5 3 3 4 2 2 1 2 3 4 5 5 5 5 3 3 4 2 2 1 3 5 5 3 2 2 2 2 2 3 4 3 3 3 3 3 4 5 5 3 3 4 2 2 1 3 5 5 1');
INSERT INTO "music" VALUES(null,'遇见','1 1.4 2 2.4 3 3.4 3.8 4.8 5.2 5.6 6 6.4 6.8 7.4 7.8 8.2 9.2 9.6 10.2 10.6 11.2 11.8 12.4 13.4 13.8 14.2 14.6 15 15.4 16 16.4 16.8','= 0 = 9 0 9 8 8 7 6 7 8 7 8 9 0 = 0 = 9 0 9 8 8 7 6 7 8 7 8 9 8');
COMMIT;
