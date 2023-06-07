from flask import Flask, jsonify, request

from flasgger import Swagger, swag_from, LazyJSONEncoder, LazyString

import re

 

# Initialize Flask API

app = Flask(__name__)

# assign LazyJSONEncoder to app.json_encoder for Swagger to work

app.json_encoder = LazyJSONEncoder

 

# Create Swagger Config & Swagger template

swagger_template = dict(

    info = {

        'title': LazyString(lambda:'API Data Cleansing'),

        'version': LazyString(lambda:'1.0.0'),

        'description': LazyString(lambda:'Dokumentasi Cleansing data for Gold Challenge by Aryo')

        }, 

    host = LazyString(lambda: request.host)

)

swagger_config = {

        "headers":[],

        "specs":[

            {

            "endpoint":'docs',

            "route":'/docs.json'

            }

        ],

        "static_url_path":"/flasgger_static",

        "swagger_ui":True,

        "specs_route":"/docs/"

}

# Initialize Swagger from swagger_template & swagger_config

swagger = Swagger(app, template=swagger_template, config=swagger_config)

 

@swag_from('docs/home.yml', methods=['GET'])

@app.route('/', methods=['GET'])

def home():

    return jsonify(

        info="API Data Cleansing",
        author="Ahmad Fadlan Amin",


        status_code=200

        )

 

@swag_from('docs/show_data.yml', methods=['GET'])

@app.route('/show_data', methods=['GET'])

def show_data():

    data = ['data1', 'data2', 'data3']

    data_dict = {}

    for row in data:

        data_dict[row] = row

    return jsonify(

        data=data_dict,

        status_code=200

        )

    

@swag_from('docs/clean_text.yml', methods=['POST'])

@app.route('/clean_text', methods=['POST'])

def clean_text():

    text = request.form['raw_text']

    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '***', text).lower() #ngeganti non alphabet jadi diapus
#ini nanti diganti dari database dari kata kasar / kata alay

    return jsonify(raw_text=text, cleaned_text=cleaned_text)

 

if __name__ == '__main__':

    app.run()