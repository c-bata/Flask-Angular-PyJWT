from flask import Blueprint, jsonify, request, current_app, url_for
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
    return jsonify(Users=['aaa', 'bbb', 'ccc'])


@api.route('/records')
def records():
    return jsonify(Records=[0, 1, 2])
