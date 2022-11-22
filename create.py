from tinydb import TinyDB, Query

db = TinyDB('data/wisata.json')
db.insert({"id": 1,
      "name": "Pulau Samber Gelap",
      "location": "Kab. Kotabaru",
      "img": "assets/img/destinasi-wisata/samber-gelap-1.jpg",
      "rate": "4.5"})
db.insert({"id": 2,
      "name": "Air Terjun Haratai",
      "location": "Kab. Hulu Sungai Selatan",
      "img": "assets/img/destinasi-wisata/haratai.jpg",
      "rate": "4.0"})