from flask import Flask, abort, request

app = Flask(__name__)

db = {}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/getdb')
def getdb():
    id = request.args.get('id')
    if id is None:
        abort(400, description="Missing 'id' query parameter")
    if id not in db:
        abort(404, description=f"No item with id '{id}'")
    return {'id': id, 'item': get_db(id)}


@app.route('/setdb')
def setdb():
    id = request.args.get('id')
    item = request.args.get('item')
    if id is None or item is None:
        abort(400, description="Both 'id' and 'item' query parameters are required")
    set_db(id, item)
    return {'id': id, 'item': item}


def get_db(id):
    return db[id]


def set_db(id, item):
    db[id] = item
