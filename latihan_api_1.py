# Creating API with Flash amnd Swagger UI with flasgger - Trial

from flask import Flask, jsonify, request

#
#Initiate Flask app

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    welcome_msg = {
        "message": "Welcome to Flask API ",
        "version": "1.0.0",
        "author": "Ahmad Fadlan Amin"
    }
    return jsonify(welcome_msg)
    return "Sup World"


if __name__ == '__main__':
    app.run()

