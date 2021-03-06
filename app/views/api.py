from flask import (
    Blueprint, jsonify, request, current_app, url_for, g, redirect,
    session, abort
)
import sqlite3
from urllib.parse import urljoin
from werkzeug.security import generate_password_hash

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return jsonify(
        users=urljoin(request.host_url, url_for('.users')),
        records=urljoin(request.host_url, url_for('.records'))
    )


@api.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            g.db.execute(
                'insert into users (name, password_hash) values (?, ?)',
                [request.json['name'], generate_password_hash(request.json['password'])]
            )
            g.db.commit()
        except sqlite3.IntegrityError:
            return jsonify({"status": "failed"})

        cur = g.db.execute('select id, name from users where name == ?',
                           [request.json['name']])
        user = cur.fetchall()[0]
        return jsonify({
            "id": user[0],
            "name": user[1]
        })

    # GET Request
    cur = g.db.execute('select id, name from users order by id desc')
    users_dict = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return jsonify(users=users_dict)


@api.route('/records')
def records():
    return jsonify(Records=[0, 1, 2])
