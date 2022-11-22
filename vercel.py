from flask import Flask
from flask import jsonify
import urllib.request

app = Flask(__name__)
@app.route('/')
def home():
    return "KalselGo"

@app.route('/api/wisata/')
def wisata_all():
    contents = urllib.request.urlopen("https://api.npoint.io/23ec7b17de445201a198").read()
    return contents

if __name__ == '__main__':
    app.run()