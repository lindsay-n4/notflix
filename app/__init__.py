from flask import Flask, render_template
from flask_restful import Api
from .users import users_blueprint
from .api.user import UserResource

app = Flask(__name__)
api = Api(app, prefix='/api')

app.register_blueprint(users_blueprint)
api.add_resource(UserResource, '/users')

@app.route('/')
def index():
    return render_template('index.html')
