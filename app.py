from flask import Flask
from flask import jsonify
from markupsafe import escape
from tinydb import TinyDB
from tinydb import Query

app = Flask(__name__)
wisataDB = TinyDB("data/wisata.json")

@app.route("/", methods = ["GET"])
def home():
    return jsonify({"status":200})

@app.route("/api/wisata/", methods = ["GET"])
def wisata_all():
    return jsonify({"status":"200",
                    "wisata":wisataDB.all()})

@app.route("/api/wisata/<string:location>/", methods = ["GET"])
def wisata(location):
    data = Query()
    return jsonify({"status":"200",
                    "wisata":wisataDB.search(data.location == escape(location))})

@app.route("/api/wisata/details/<int:id>/", methods = ["GET"])
def wisata_details(id):
    data = Query()
    return jsonify({"status":"200",
                    "wisata":wisataDB.search(data.id == id)})

if __name__ == "__main__":
    app.run()
