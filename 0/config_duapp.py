#-*- coding:utf-8 -*-
__author__ = 'YangZhiyong'

import os
import sys
from bae.core import const
import pymongo

path = os.path.dirname(os.path.abspath(__file__)) + '/flask_restful'
if path not in sys.path:
    sys.path.insert(1, path)

DB_Host = const.MONGO_HOST
DB_Port = int(const.MONGO_PORT)
DB_Name = 'nNnEghIugFZsYVuYyIHK'


DB_Connection = pymongo.Connection(host=DB_Host, port=DB_Port)
DB_Database = DB_Connection[DB_Name]
DB_Database.authenticate(const.MONGO_USER, const.MONGO_PASS)


