#Create API with Flask

from flask import Flask, jsonify, render_template


apps = Flask(__name__)

#----ini fungsi api yang get----

@apps.route("/", methods=["GET"])
def halaman_utama():
    return "Halo, Selamat Datang di Halaman utama"

@apps.route("/halaman2", methods=["GET"])
def halaman_dua():
    return "Halo, Selamat Datang di Halaman kedua"

@apps.route("/<string:nama>", methods=["GET"])
def welcoming_user(nama):
    return f"Halo, Selamat Datang di Halaman {nama}"


#ini kalo mau buat kalimat nya lebih dari satu 
@apps.route("/halaman3", methods=["GET"])

def halaman_tiga():

    return """

<h1>Halo, Selamat Datang di Halaman Tiga</h1>

<p>Ini adalah paragraf</p>

<ul>

    <li>Ini adalah list 1</li>

    <li>Ini adalah list 2</li>

<ul>

"""

#-- ini fungsi api yang post---

@apps.route("/penjumlahan", methods=["POST"])

def penjumlahan():

    """ 

    To request using curl:

    curl -X POST -H "Content-Type: application/json" -d '{"angka1": 1, "angka2": 2}' http://localhost:5000/penjumlahan

    """

    data = request.json

    hasil = int(data["angka1"]) + int(data["angka2"])

    return {"hasil": hasil}

if __name__ == "__main__":
    apps.run() 
    # apps.run(port=8000, debug=True)
    #ini port atau linknya diubah jadi 8000
    #ini debug=True , setiap kita save akan dijalanin lagi atau diupdate
    #not recommended buat beginner