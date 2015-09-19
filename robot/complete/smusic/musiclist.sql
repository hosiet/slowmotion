PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE musicdata (
id INTEGER PRIMARY KEY,
filename TEXT NOT NULL,
havenote INTEGER NOT NULL);
INSERT INTO "musicdata" VALUES(null,'年轻的战场.mp3',0);
INSERT INTO "musicdata" VALUES(null,'光荣啊中国共青团(young).mp3',0);
INSERT INTO "musicdata" VALUES(null,'光荣啊,中国共青团.mp3',0);
INSERT INTO "musicdata" VALUES(null,'困兽之斗.mp3',0);
INSERT INTO "musicdata" VALUES(null,'节奏1.mp3',0);
INSERT INTO "musicdata" VALUES(null,'节奏2.mp3',0);
INSERT INTO "musicdata" VALUES(null,'节奏3.mp3',0);
INSERT INTO "musicdata" VALUES(null,'节奏4.mp3',0);
COMMIT;
