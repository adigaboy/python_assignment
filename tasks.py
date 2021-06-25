import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
from celery import Celery
from database import mydatabase

BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
app = Celery('tasks', backend=CELERY_RESULT_BACKEND, broker=BROKER_URL)

@app.task
def multiple(dbm, id, arr):
    result = 1
    for i in arr:
        result *= i
    dbm.updateResult(id, result)