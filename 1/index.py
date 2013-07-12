#-*- coding:utf-8 -*-

from bae.core import const
import pymongo
 
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body = ""
    db_name = 'nNnEghIugFZsYVuYyIHK'
    con = pymongo.Connection(host = const.MONGO_HOST, port = int(const.MONGO_PORT))
    db = con[db_name]
    db.authenticate(const.MONGO_USER, const.MONGO_PASS)
    #获取该db所有的collection
    body = db.collection_names()
    con.disconnect()
    return body
 
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)