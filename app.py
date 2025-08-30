from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary storage (use a DB in production)
bus_location = {"lat": None, "lng": None}

@app.route('/update-location', methods=['POST'])
def update_location():
    global bus_location
    data = request.json
    bus_location['lat'] = data.get('lat')
    bus_location['lng'] = data.get('lng')
    return jsonify({"status": "success", "message": "Location updated"}), 200

@app.route('/get-location', methods=['GET'])
def get_location():
    return jsonify(bus_location), 200

if __name__ == '__main__':
    app.run(debug=True)
