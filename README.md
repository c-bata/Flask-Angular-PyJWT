# Research Record

## Structure

- Python3.5/Flask
- SQLite3
- PyJWT
- AngularJS

## Setup

- create tables: `$ sqlite3 db.sqlite3 < schema.sql`
- `cd client; npm install`
- `python manage.py runserver -p 10000 -h 0.0.0.0`

#### nginx config

```
server {
  location = /favicon.ico {
    access_log off;
    log_not_found off;
  }

  location / {
    proxy_set_header Host $host;
    root /<path to repo>/Flask-Angular-PyJWT/client/;
  }

  location /api {
    proxy_set_header Host $host;
    proxy_pass http://127.0.0.1:10000;
  }
}
```


## License

This software is licensed under the MIT License.

