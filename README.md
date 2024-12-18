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
- **Frontend**: HTML, Bootstrap  
- **Backend**: Python Flask for face recognition and location tracking  
- **Database**: SQLite for storing student data, attendance records, and location logs using inbuilt Django modules  
- **User Authentication**: Django CSRF tokens for secure login management  
- **Location Tracking**: Geolocation API for live tracking  
- **Face Recognition**: OpenCV and DeepFace library for face ID validation  

## Installation  
To set up the Student Safety Tracker application locally, follow these steps:

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/StudentSafetyTracker.git
   cd StudentSafetyTracking_5thSem
   ```


2. Set up the virtual environment for the face recognition module:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
```
 #After Setting up the environment it looks like this 
 (venv) path/StudentSafetyTracking_5thSem

 3. Setup the django and install all other requirements
```bash
   cd miniproject (move to project folder)
   cd locationtrack(move to user's app)
   pip install django
   pip install -r requirements.txt
```
 
4.After install all the requirements split the terminal into two parts for flask server and django application 

Move to miniproject directory and make database migrations
```bash
   (venv) python manage.py makemigrations
   (venv) python manage.py migrate
```

5. Run Project:
```bash
   cd ..
   cd miniproject
```

6. Start the django server:
```bash
   (venv) python manage.py runsever
```

7. For the backend(Flask server):Remeber to be in locationtrack directory and ensure everything is installed and running on virtual environment
```bash
(venv) python validatelocation.py
```

## Screenshots  
### Login Page  ![1getstartedpng](https://github.com/user-attachments/assets/0f757b3e-b335-46ab-a53d-866191387532)


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

