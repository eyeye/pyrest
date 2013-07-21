#-*- coding:utf-8 -*-

__author__ = 'EYE'


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

from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from bson import json_util

if 'SERVER_SOFTWARE' in os.environ:
    from config_duapp import DB_Database
else:
    from config_localhost import DB_Database



User_AddParser = reqparse.RequestParser()
User_AddParser.add_argument('account', type=str, help='account string')
User_AddParser.add_argument('password', type=str, help='password string')
User_AddParser.add_argument('email', type=str, help='email string')

response_fields = {
    'status': fields.String,
    'account': fields.String,
}


class User(Resource):
    def get(self):
        userList = DB_Database.user.find()
        print userList
        # print json_util.dumps(userList)
        return json_util.dumps(userList, default=json_util.default)
        # return json_util.dumps(userList, separators=(',',':'))

    def put(self):
        return 'PutUser'

    # @marshal_with(response_fields)
    def post(self):
        args = User_AddParser.parse_args()
        print args

        user = DB_Database.user.find_one({'account': args['account']})
        print user

        if user is None:
            id = DB_Database.user.insert(args)
            print id
            return {'status':'succeed', 'account':args['account']}
        else:
            return {'status':'failed', 'account':args['account']}


    def delete(self):
        return 'DeleteUser'



