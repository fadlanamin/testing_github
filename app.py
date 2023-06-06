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

if __name__ == "__main__":
    apps.run()