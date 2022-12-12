import json
from flask import Blueprint, render_template

with open('users.json', 'r') as f:
    collection = json.load(f)

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder = 'templates',
    url_prefix = '/users')

@users_blueprint.route('/')
def index():
    return render_template('users/index.html', users = sorted(collection, key = lambda x: x['username']))
