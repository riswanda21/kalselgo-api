from flask import Flask
from flask import jsonify
from tinydb import TinyDB, Query

wisataDB = TinyDB('data/wisata.json')
@app.route('/api/wisata/')
def wisata_all():
    return jsonify({'status':'200',
                    'wisata':wisataDB.all()})

@app.route('/api/wisata/<string:location>/')
def wisata(location):
    data = Query()
    return jsonify({'status':'200',
                    'wisata':wisataDB.search(data.location == location)})

