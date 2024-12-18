import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from opencage.geocoder import OpenCageGeocode
import django
import sys
import logging
from flask import session
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproject.settings')  # Replace 'locationtrack.settings' with your actual settings module
django.setup()  # Initialize Django

# Import your Django models after setting up Django
from locationtrack.models import Student

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key to store session data securely
CORS(app, origins=["http://127.0.0.1:8000"])

# Initialize OpenCage Geocode API
OPEN_CAGE_API_KEY = os.getenv('OPENCAGE_API_KEY', 'YOURAPIKEY') 
geocoder = OpenCageGeocode(OPEN_CAGE_API_KEY)

# Updated Flask route
@app.route('/validate_location', methods=['POST'])
def validate_location():
    try:
        data = request.get_json()
        logging.debug(f"Received request payload: {data}")
        if not data:
            logging.error("No JSON payload received.")
            return jsonify({"is_valid": False, "error": "No JSON payload received."}), 400

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        user_email = data.get('email')

        if not all([latitude, longitude, user_email]):
            logging.error("Missing latitude, longitude, or email in the request.")
            return jsonify({"is_valid": False, "error": "Latitude, longitude, and email are required."}), 400

        # Query the student
        try:
            user = Student.objects.get(email=user_email)
            logging.debug(f"User found: {user}")
        except Student.DoesNotExist:
            logging.warning(f"User with email {user_email} not found.")
            return jsonify({"is_valid": False, "error": "User not found."}), 404

        stored_country = user.nationality
        #stored_country = "China"
        logging.debug(f"Stored country for user: {stored_country}")

        # Reverse geocode
        results = geocoder.reverse_geocode(latitude, longitude)
        logging.debug(f"Geocoder results: {results}")

        if not results:
            logging.error("Unable to fetch location details from geocoder.")
            return jsonify({"is_valid": False, "error": "Unable to fetch location details."}), 500

        user_country = results[0]['components'].get('country')
        logging.debug(f"User's actual country: {user_country}")

        if user_country and user_country.lower() == stored_country.lower():
            logging.info(f"Validation successful for user: {user_email}")
            
            # Store country in session
            session['user_country'] = user_country

            return jsonify({"is_valid": True, "user_country": user_country})
        else:
            logging.info(f"Validation failed for user: {user_email}. Detected country: {user_country}")
            return jsonify({"is_valid": False, "user_country": user_country or "Unknown"})

    except Exception as e:
        logging.exception("An exception occurred during location validation.")
        return jsonify({"is_valid": False, "error": f"Exception: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
