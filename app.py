import cassiopeia as cass
from cassiopeia import Account
import datetime
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import math
from io import BytesIO
import os
import base64
cass.set_riot_api_key("RGAPI-57803bce-9eaa-4491-bc1f-82c8e2a260e9") 

app = Flask(__name__)
CORS(app)

def get_summoner_info(name: str, tagline: str, region: str):
    account = Account(name=name, tagline=tagline, region=region)
    summoner = account.summoner
    img = summoner.profile_icon.image
    buffered = BytesIO()
    img.save(buffered, format='png')
    encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    result = {
        'name': account.name_with_tagline,
        'level': summoner.level,
        'profilePicture': f"data:image/png;base64,{encoded_image}"
        # 'profilePicture': send_file(summoner.profile_icon.image, mimetype='image\png')
    }
    return result


@app.route('/summonerInfo', methods = ['POST'])
def get_data():
    data = request.json
    name = data.get('name')
    tagline = data.get('tagline')
    region = data.get('region')
    result= get_summoner_info(name, tagline, region)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)