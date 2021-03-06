drop table if exists users;
create table users (
  id integer primary key autoincrement,
  name text not null unique,
  password_hash text not null
);

drop table if exists research_records;
create table research_records (
  id integer primary key autoincrement,
  day date not null,
  start_time datetime not null,
  end_time datetime not null,
  detail text,
  foreign key (id) references users(id)
);
