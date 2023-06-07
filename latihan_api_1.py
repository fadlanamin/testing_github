# Creating API with Flash amnd Swagger UI with flasgger - Trial

from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from, LazyString, LazyJSONEncoder

#Initiate Flask app
app = Flask(__name__)

# Assign LazyJSONEncoder to appp.json_encoder for Swagger UI
app.json_encoder = LazyJSONEncoder

#Create swagger Template & Config Object
swagger_template = {
    "info": {
        "title": LazyString(lambda: "Flask API"),
        "version": LazyString(lambda: "1.0.0"),
        "description": LazyString(lambda: "Latihan membuat API dengan Flask")
    },
    "host": LazyString(lambda: request.host),
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "docs", #ini nanti di link nya kalo ditambah /docs/ akan muncul ke swagger ui
            "route": "/docs.json"
        }
    ],
    "static_url_path": "/flassger_static",
    "swagger_ui":True,
    "specs_route": "/docs/"

}

# Initialize swagger UI from template & config
swagger = Swagger(app, template=swagger_template, config=swagger_config)


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

