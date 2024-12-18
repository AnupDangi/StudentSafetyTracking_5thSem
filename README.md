# Student Safety Tracker

## Overview  
**Student Safety Tracker** is an innovative application designed for the safety and attendance tracking of students studying abroad. With features such as live location tracking, browser-based face ID validation, and robust attendance history management, this web application ensures students' safety while streamlining attendance processes for educational institutions. The project also includes safeguards against location manipulation through VPNs or paid apps.

## Project Goals  
This project aims to create a scalable, user-friendly system that prioritizes students' safety and attendance tracking by incorporating:

- **Real-time location tracking**
- **Face ID-based attendance verification**
- **Attendance history management**

## How It Works  
The Student Safety Tracker leverages geolocation technologies and advanced browser-based facial recognition to validate attendance and ensure safety. By integrating live location tracking with location spoofing countermeasures, the system ensures the authenticity of the attendance process and provides peace of mind for institutions and parents alike.

## Features  
- **Location Tracking**: Accurate real-time location tracking with safeguards against manipulation.
- **Face Attendance System**: Browser-based face ID validation for reliable attendance tracking.
- **Attendance History**: A comprehensive history of attendance, accessible at any time.
- **Scalability**: Built to handle large-scale usage by educational institutions.

## Technologies Used  
- **Frontend**: React, CSS, JavaScript
- **Backend**: Python Flask for face recognition and location tracking
- **Database**: MongoDB for storing student data, attendance records, and location logs
- **User Authentication**: Node.js for secure login management
- **Location Tracking**: Geolocation API for live tracking
- **Face Recognition**: OpenCV and Dlib for face ID validation

## Installation  
To set up the Student Safety Tracker application locally, follow these steps:

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/StudentSafetyTracker.git
   cd StudentSafetyTracker
   ```

2. Install the necessary dependencies for both the frontend and backend. Refer to the imports for detailed requirements.

For the frontend:
```bash
cd src
npm install
```

For the backend:
```bash
cd backend
pip install -r requirements.txt
```

**Dependencies:**
- Flask
- OpenCV
- Dlib
- Geopy
- Flask-CORS

3. Set up the MongoDB database and ensure it is running.

4. Start the backend server:
```bash
python app.py
```

5. Start the frontend server:
```bash
npm start
```

6. Set up the virtual environment for the face recognition module:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
```

Run the face recognition module:
```bash
(venv) python face_recognition_module.py
```

7. Run the location tracking service:
```bash
(venv) python location_service.py
```

## Screenshots  
### Login Page  
![Login Page](https://example.com/path-to-login-page-image)

### Dashboard  
![Dashboard](https://example.com/path-to-dashboard-image)

### Attendance History  
![Attendance History](https://example.com/path-to-attendance-history-image)

### Live Location Tracking  
![Live Location Tracking](https://example.com/path-to-location-tracking-image)

## Contributing  
Contributions are always welcome.  
Feel free to use this project and modify it based on your requirements. Create pull requests to suggest improvements or add new features.

## License  
This project is licensed under the MIT License - see the LICENSE file for details.

