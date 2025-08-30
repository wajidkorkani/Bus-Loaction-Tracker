# Device Tracker

A simple Flask-based API that provides the server's current geographical location using IP geolocation.

## Features
- Returns server latitude and longitude via `/get-location` endpoint
- Uses [ipapi.co](https://ipapi.co/) for IP-based geolocation
- CORS enabled for cross-origin requests

## Requirements
- Python 3.7+
- Flask
- Flask-CORS
- requests

## Installation
1. Clone the repository:
	```powershell
	git clone https://github.com/wajidkorkani/Device-Tracker.git
	cd Device-Tracker
	```
2. Install dependencies:
	```powershell
	pip install flask flask-cors requests
	```

## Usage
Run the Flask app:
```powershell
python app.py
```

The API will be available at `http://localhost:5000/get-location`.

## API Endpoint
### `GET /get-location`
Returns the server's latitude and longitude as JSON:
```json
{
  "lat": ,
  "lng": ,
}
```

## License
MIT