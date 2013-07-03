#-*- coding:utf-8 -*-
from bae.core import const
from flask import Flask, g, request
import os
import sys

# sys.path.insert(0, const.APP_DIR)

path = os.path.dirname(os.path.abspath(__file__)) + '/flask_restful'
if path not in sys.path:
  sys.path.insert(1, path)

from flask_restful import Resource, Api

app = Flask(__name__)
app.debug = True

api = Api(app)

# @app.route('/')
# def hello():
#     return "Hello, world! - Flask\n"


class TodoSimple(Resource):
    def get(self):
        return {"Hello": "World!"}


api.add_resource(TodoSimple, '/<string:todo_id>')

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

