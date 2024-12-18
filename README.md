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
   git clone https://github.com/AnupDangi/StudentSafetyTracking_5thSem.git
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
   cd locationtrack (move to user's app)
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

### Landing Page
![1getstartedpng](https://github.com/user-attachments/assets/0f757b3e-b335-46ab-a53d-866191387532)

### Signup Page 
![2signup](https://github.com/user-attachments/assets/d9a3cc13-5338-47ed-9dad-f7e91e92ccb9)

### Login Page 
![4 login](https://github.com/user-attachments/assets/b353e7c4-5c01-49ff-937c-e662f5ea2fee)

### Dashboard 
![5 homepage](https://github.com/user-attachments/assets/de51b400-2ed4-4fc2-870b-129711280148)

### Live Location Tracking 
![6 Validatelocation](https://github.com/user-attachments/assets/7b8edf63-fb6e-42d6-b022-84cbbabef129)

### When singup form's country doesnot matches during location validation 
![Locationnotvalidated](https://github.com/user-attachments/assets/a109fe31-5a75-49c4-ae06-27542f90a5f7)

### Face Validation 
![7 face_validation](https://github.com/user-attachments/assets/23ec0716-6a63-475e-bf02-182112525fbb)
![8 VerifyAttendance](https://github.com/user-attachments/assets/d0ab4a29-ca2a-4fe5-b36c-d904c00e3db4)

### Attendance History  
![9 History](https://github.com/user-attachments/assets/8e5a3075-c472-4884-be70-3a7ebcf4d1cc)

### Profile
![10 Profile](https://github.com/user-attachments/assets/a408afaf-d4fe-4357-9ee1-e929f76a1c2a)

### Code working validation
![11 Codetemplates](https://github.com/user-attachments/assets/3a70517c-5b78-43b1-a207-d462d6378df6)

### face_recognitionmodel using tkinter before integration in web
![image](https://github.com/user-attachments/assets/db3b1242-6eb3-4e1e-90f9-ea98697a03e8)

### Admin Panel with Attendance tracking 
![AdminPanelwhennoalert](https://github.com/user-attachments/assets/a39febb3-f3c8-4afc-b727-b7d3f8576b60)

### Alert Message on User's Dashboard 
![alertmessage](https://github.com/user-attachments/assets/a4236ff4-c7b3-402a-ba03-60ae93763b95)

### Alert Message on Admin Panel
![AdminPanelwhennoalert](https://github.com/user-attachments/assets/5f220d65-4a8c-45c8-a1d8-d36b43f9b9f3)

## Contributing  
Contributions are always welcome.  
Feel free to use this project and modify it based on your requirements. Create pull requests to suggest improvements or add new features.

## License  
This project is licensed under the MIT License - see the LICENSE file for details.

