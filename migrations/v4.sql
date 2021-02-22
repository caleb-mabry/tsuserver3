CREATE TABLE IF NOT EXISTS area(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT 
);
INSERT INTO area(name) SELECT DISTINCT room_name name from ic_events WHERE NOT EXISTS (SELECT NAME FROM AREA WHERE area.NAME == ic_events.room_name)
