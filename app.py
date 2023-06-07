#Create API with Flask

from flask import Flask, jsonify, render_template


apps = Flask(__name__)

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

if __name__ == "__main__":
    apps.run()