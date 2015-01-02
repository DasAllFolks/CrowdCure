drop table if exists locations;

create table locations (
  id integer primary key autoincrement,
  latitude real,
  longitude real;
  timestamp integer;
);
