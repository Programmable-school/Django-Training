# db command
```sh
# db create
createdb djangoapp

# db delete
dropdb djangoapp

# db connect
psql djangoapp
```

## psql command

```sh
# terminate
\q

# show database
\l

# show table list
\d

# create table
CREATE TABLE languages ( name varchar(64), developer varchar(128), date date );

# delete table
DROP TABLE languages;

# insert data
INSERT INTO languages VALUES ('Python', 'Guido Van Rossum', '1991-01-01');
INSERT INTO languages (name, developer, date) VALUES ('Ruby', 'Matumoto Yukihiro', '1995-01-01');
INSERT INTO languages (name, developer, date) VALUES ('C++', 'Bjarne Stroustrap', '1983-01-01');
INSERT INTO languages (name, developer, date) VALUES ('PHP', 'Rasmus Lerdorf', '1995-01-01');

# get data
SELECT name, developer, date FROM languages;
SELECT * FROM languages;
SELECT * FROM languages WHERE developer = 'Matumoto Yukihiro';
SELECT * FROM languages WHERE developer = 'Matumoto Yukihiro' AND name = 'Ruby';
SELECT * FROM languages WHERE developer = 'Matumoto Yukihiro' OR developer = 'Guido Van Rossum';
SELECT * FROM languages ORDER BY date;

# update data
UPDATE languages SET developer = 'まつもとゆきひろ' WHERE developer = 'Matumoto Yukihiro';

# delete data
DELETE FROM languages WHERE developer = 'Rasmus Lerdorf';

# create user
CREATE USER django;

# change owner
ALTER DATABASE djangoapp OWNER TO django;

# current user
SELECT current_user;

# change user
\connect - django;
```
