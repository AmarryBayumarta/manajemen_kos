from app import db
from models.user import User

class Penghuni(User, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    kamar_id = db.Column(db.Integer)

    def __init__(self, nama, kamar_id):
        User.__init__(self, nama)
        self.kamar_id = kamar_id

    # polymorphism
    def info(self):
        return f"Penghuni kos: {self.nama}"