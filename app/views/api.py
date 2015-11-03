from flask import Blueprint, jsonify, request, current_app, url_for, g
from urllib.parse import urljoin

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return jsonify(
        users=urljoin(request.host_url, url_for('.users')),
        records=urljoin(request.host_url, url_for('.records'))
    )


@api.route('/users')
def users():
    cur = g.db.execute('select id, name from users order by id desc')
    users_dict = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return jsonify(users=users_dict)


@api.route('/records')
def records():
    return jsonify(Records=[0, 1, 2])
