from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from celery import Celery
from database import mydatabase
import json
import tasks

app = Celery('tasks', broker='pyamqp://guest@localhost//')

def GET(path, request):
    try:
        result = dbms.getResult(request.matchdict['result_id'])
    except Exception as e:
        print(e)
    else:
        return {"result":result}

def POST(request):
    for client_id in request.json_body:
        dbms.insert(client_id, request.json_body[client_id])
        tasks.multiple(dbms, client_id, request.json_body[client_id])
    return Response()

if __name__ == '__main__':
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite')
    with Configurator() as config:
        config.add_route('get', '/result/{result_id}')
        config.add_view(GET, route_name='get')
        config.add_route('post', '/upload')
        config.add_view(POST, route_name='post')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()