PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE musicdata (
id INTEGER PRIMARY KEY,
filename TEXT NOT NULL,
havenote INTEGER NOT NULL);
INSERT INTO "musicdata" VALUES(1,'年轻的战场.mp3',0);
COMMIT;
