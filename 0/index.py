#-*- coding:utf-8 -*-

import os
import sys


if 'SERVER_SOFTWARE' in os.environ:
    from bae.core import const
else:
    pass



from flask import Flask, g, request

# sys.path.insert(0, const.APP_DIR)

path = os.path.dirname(os.path.abspath(__file__)) + '/flask_restful'
if path not in sys.path:
    sys.path.insert(1, path)

from flask_restful import Resource, Api


app = Flask(__name__)
app.debug = True
api = Api(app)


#############################################################


class HelloEYE(Resource):
    def get(self):
        return {'hello': 'YangZhiyong'}

api.add_resource(HelloEYE, '/eye')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'EYE', 'APP_DIR': 'HAHA'}

api.add_resource(HelloWorld, '/')


class HelloWho(Resource):
    def get(self, who):
        return {'hello': who}

api.add_resource(HelloWho, '/<string:who>')


#############################################################

if 'SERVER_SOFTWARE' in os.environ:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
else:
    if __name__ == '__main__':
        app.run(debug=True)

