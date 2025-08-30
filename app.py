from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Get server's location at startup using IP geolocation API
def get_server_location():
    try:
        response = requests.get("https://ipapi.co/json/")
        if response.status_code == 200:
            data = response.json()
            return {"lat": data.get("latitude"), "lng": data.get("longitude")}
    except Exception as e:
        print("Error getting server location:", e)
    return {"lat": None, "lng": None}


@app.route('/get-location')
def get_location():
    # Always get fresh server location when called
    return jsonify(get_server_location()), 200

if __name__ == '__main__':
    app.run(debug=True)
