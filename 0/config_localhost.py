#-*- coding:utf-8 -*-
__author__ = 'YangZhiyong'




import pymongo

DB_Host = '127.0.0.1'
DB_Port = 27017
DB_Name = 'local'

DB_Connection = pymongo.Connection(host=DB_Host, port=27017)
DB_Database = DB_Connection[DB_Name]

