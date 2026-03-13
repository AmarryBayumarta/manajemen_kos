from app import db

class Kamar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomor = db.Column(db.String(10))
    harga = db.Column(db.Integer)
    status = db.Column(db.String(20))

    def __init__(self, nomor, harga, status):
        self.nomor = nomor
        self.harga = harga
        self.status = status