#-*- coding:utf-8 -*-

import os
import sys
from Crypto.PublicKey import RSA
import json

if 'SERVER_SOFTWARE' in os.environ:
    from config_duapp import DB_Database
else:
    from config_localhost import DB_Database



from flask import Flask, g, request

# sys.path.insert(0, const.APP_DIR)

path = os.path.dirname(os.path.abspath(__file__)) + '/flask_restful'
if path not in sys.path:
    sys.path.insert(1, path)

from flask_restful import Resource, Api, reqparse, abort
# from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.debug = True
api = Api(app)


################## Mongo ###########################################

# if 'SERVER_SOFTWARE' in os.environ:
#     app.config['MONGO_HOST'] = const.MONGO_HOST
#     app.config['MONGO_PORT'] = const.MONGO_PORT
#     app.config['MONGO_DBNAME'] = 'GeEBBeqAoMglOIEuqZaD'
# else:
#     app.config['MONGO_HOST'] = '127.0.0.1'
#     app.config['MONGO_PORT'] = 27017
#     app.config['MONGO_DBNAME'] = 'local'

# app.config['MONGO_DBNAME'] = 'local'
# mongo = PyMongo(app, config_prefix='MONGO')

#############################################################


class HelloEYE(Resource):
    def get(self):
        return {'hello': 'YangZhiyong'}

api.add_resource(HelloEYE, '/eye')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'EYE', 'path': path, 'APP_DIR': 'NONE'}

api.add_resource(HelloWorld, '/')


class HelloWho(Resource):
    def get(self, who):
        return {'hello': who}

api.add_resource(HelloWho, '/<string:who>')


Todos = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


def abort_no_exist(todo_id):
    if todo_id not in Todos:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

class Todo(Resource):
    def get(self, todo_id):
        abort_no_exist(todo_id)
        return {todo_id: Todos[todo_id]}

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        Todos[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        abort_no_exist(todo_id)
        del Todos[todo_id]
        return '', 204

api.add_resource(Todo, '/<string:todo_id>')



class TodoList(Resource):
    def get(self):
        return Todos

api.add_resource(TodoList, '/todolist')


class DBTest(Resource):
    def get(self):

        print 'findone'
        todo = DB_Database.todos.find_one()
        print json_util.dumps(todo)

        print 'find'
        list = DB_Database.todos.find()
        # print json_util.dumps(list)
        return json_util.dumps(list, default=json_util.default)
        # print json_util.dumps({'a': 'b', 'c': 'd'})
        # return json_util.dumps({'a': 'b', 'c': 'd'})

    def put(self):
        print 'put'

api.add_resource(DBTest, '/mongotest')



class RSA_Test(Resource):
    def get(self):
        # print 'RSA_Test put'

        key = RSA.generate(1024)
        # '========== pubkey ==================='
        # print key
        # print key.exportKey('PEM')

        # print '========== pubkey ==================='
        pubkey = key.publickey()
        # print pubkey.exportKey('PEM')

        return key.exportKey('PEM')

api.add_resource(RSA_Test, '/rsatest')



class UserManager(Resource):
    pass

api.add_resource(UserManager, '/user')




#############################################################

if 'SERVER_SOFTWARE' in os.environ:
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
else:
    if __name__ == '__main__':
        app.run(debug=True)

