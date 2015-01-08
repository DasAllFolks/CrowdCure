drop table if exists locations;

create table locations (
  id integer primary key autoincrement,
  latitude real not null,
  longitude real not null,
  timestamp integer not null
);
