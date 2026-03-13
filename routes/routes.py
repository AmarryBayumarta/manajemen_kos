from app import app, db
from flask import render_template, request, redirect
from models.kamar import Kamar


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kamar")
def kamar():
    data = Kamar.query.all()
    return render_template("kamar.html", kamar=data)


@app.route("/tambah_kamar", methods=["GET","POST"])
def tambah_kamar():

    if request.method == "POST":
        nomor = request.form["nomor"]
        harga = request.form["harga"]
        status = request.form["status"]

        kamar = Kamar(nomor, harga, status)

        db.session.add(kamar)
        db.session.commit()

        return redirect("/kamar")

    return render_template("tambah_kamar.html")

@app.route("/edit_kamar/<int:id>", methods=["GET","POST"])
def edit_kamar(id):

    kamar = Kamar.query.get_or_404(id)

    if request.method == "POST":
        kamar.nomor = request.form["nomor"]
        kamar.harga = request.form["harga"]
        kamar.status = request.form["status"]

        db.session.commit()

        return redirect("/kamar")

    return render_template("edit_kamar.html", kamar=kamar)


@app.route("/delete_kamar/<int:id>")
def delete_kamar(id):

    kamar = Kamar.query.get_or_404(id)

    db.session.delete(kamar)
    db.session.commit()

    return redirect("/kamar")

@app.route("/list_kamar")
def list_kamar():

    data = Kamar.query.all()

    daftar_kamar = []

    for k in data:
        daftar_kamar.append(k.nomor)

    return str(daftar_kamar)