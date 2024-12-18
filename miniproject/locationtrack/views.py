
from datetime import timedelta
from time import localtime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .forms import StudentForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout  # Rename imported login function
import os
import cv2
import numpy as np
from django.utils.timezone import now
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from deepface import DeepFace
from scipy.spatial.distance import cosine
from locationtrack.models import Student, Attendance
import logging
import requests
from django.utils import timezone
from flask import session

FLASK_BACKEND_URL = 'http://127.0.0.1:5000/validate_location'

USER_DB = "user_images"
os.makedirs(USER_DB, exist_ok=True)

def getstarted(request):
    return render(request, 'getstarted.html')


def signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            if Student.objects.filter(email=email).exists():
                messages.error(request, "An account with this email already exists.")
                return render(request, 'signup.html', {'form': form})

            student = Student(
                full_name=form.cleaned_data['full_name'],
                email=email,
                password=make_password(form.cleaned_data['password']),
                age=form.cleaned_data['age'],
                nationality=form.cleaned_data['nationality'],
                college=form.cleaned_data['college'],
                college_address=form.cleaned_data['college_address'],
                city=form.cleaned_data['city'],
                location_consent=form.cleaned_data['location_consent']
            )
            student.save()
            messages.success(request, "Account created successfully! Please login.",)
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm()

    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log user in
            login(request, user)  # This logs the user into the session
            return redirect('/home/')  # This will redirect to the home page
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
    
@csrf_exempt
@login_required(login_url='/login/')
def add_user_face(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image')

        logging.debug("Received request to add face for user: %s", user.full_name)

        if not image:
            logging.warning("Image missing in request")
            return JsonResponse({"message": "Image required"}, status=400)

        try:
            # Generate folder name
            email_numeric = ''.join(filter(str.isdigit, user.email))
            folder_name = f"{user.full_name.replace(' ', '_')}_{email_numeric}"
            user_path = os.path.join(USER_DB, folder_name)
            os.makedirs(user_path, exist_ok=True)
            logging.debug("Directory created or already exists: %s", user_path)

            # Save image
            image_path = os.path.join(user_path, f"face_{len(os.listdir(user_path))}.jpg")
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            logging.info("Image saved at: %s", image_path)

            return JsonResponse({"message": "Face registration successful"})
        except Exception as e:
            logging.exception("An error occurred during face registration")
            return JsonResponse({"message": str(e)}, status=500)

@csrf_exempt
@login_required(login_url='/login/')
def is_face_registered(request):
    user = request.user
    # Construct folder name based on user info
    email_numeric = ''.join(filter(str.isdigit, user.email))
    folder_name = f"{user.full_name.replace(' ', '_')}_{email_numeric}"
    user_path = os.path.join(USER_DB, folder_name)

    # Check if the folder exists
    is_registered = os.path.exists(user_path)
    logging.debug(f"User {user.full_name} face registration status: {is_registered}")
    return JsonResponse({"registered": is_registered})

@csrf_exempt
@login_required(login_url='/login/') 
def verify_attendance(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image')

        logging.debug("Received request to verify attendance for user: %s", user.full_name)

        if not image:
            logging.warning("Image missing in request")
            return JsonResponse({"message": "Image required"}, status=400)

        # Construct the folder name
        email_numeric = ''.join(filter(str.isdigit, user.email))
        folder_name = f"{user.full_name.replace(' ', '_')}_{email_numeric}"
        user_path = os.path.join(USER_DB, folder_name)

        # Path for the temporary file
        temp_path = os.path.join(USER_DB, "temp_verify.jpg")
        try:
            # Save the temporary uploaded image
            with open(temp_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            logging.debug("Temporary verification image saved at: %s", temp_path)

            # Check if the folder exists
            if not os.path.exists(user_path):
                logging.warning("No face registered for user: %s", user.full_name)
                os.remove(temp_path)
                return JsonResponse({"message": "No face registered for this user", "verified": False})

            # Generate live embedding for the temporary image
            live_embedding = DeepFace.represent(temp_path, model_name='VGG-Face', enforce_detection=False)
            live_embedding = live_embedding[0]['embedding']
            logging.debug("Live embedding generated")

            # Compare with stored embeddings in the user's folder
            for img_name in os.listdir(user_path):
                stored_img_path = os.path.join(user_path, img_name)
                stored_embedding = DeepFace.represent(stored_img_path, model_name='VGG-Face', enforce_detection=False)
                stored_embedding = stored_embedding[0]['embedding']
                logging.debug("Comparing with stored image: %s", img_name)

                # Calculate cosine distance
                distance = cosine(live_embedding, stored_embedding)
                logging.debug("Cosine distance calculated: %f", distance)

                if distance < 0.4:  # Threshold for similarity
                    # Record attendance
                    Attendance.objects.create(student=user)
                    logging.info("Attendance recorded successfully for user: %s", user.full_name)
                    os.remove(temp_path)
                    return JsonResponse({"message": "Attendance recorded successfully", "verified": True})

            # If no match is found
            os.remove(temp_path)
            logging.info("Face verification failed for user: %s", user.full_name)
            return JsonResponse({"message": "Face verification failed", "verified": False})

        except Exception as e:
            logging.exception("An error occurred during attendance verification")
            if os.path.exists(temp_path):
                os.remove(temp_path)
            return JsonResponse({"message": str(e), "verified": False})



def record_attendance(request):
    if request.method == "POST":
        data = request.POST
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        email = request.user.email  # Assuming user is logged in and has an email.

        if not all([latitude, longitude]):
            return JsonResponse({"success": False, "error": "Latitude and longitude are required."}, status=400)

        try:
            # Send data to Flask backend
            response = requests.post(FLASK_BACKEND_URL, json={
                "latitude": latitude,
                "longitude": longitude,
                "email": email
            })

            flask_data = response.json()

            if not flask_data.get('is_valid'):
                return JsonResponse({"success": False, "error": flask_data.get('error', "Invalid location.")}, status=400)

            # Get city from Flask response
            city = flask_data.get('user_city', 'Unknown')

            # Save attendance record
            Attendance.objects.create(
                timestamp=now(),
                city=city,
                user=request.user
            )
            return JsonResponse({"success": True, "city": city})

        except Exception as e:
            return JsonResponse({"success": False, "error": f"Error validating location: {str(e)}"}, status=500)
        


@login_required(login_url='/login/') 
def home(request):
    user = request.user
    alert_needed = False

    # Get the latest attendance record for the user
    last_attendance = Attendance.objects.filter(student=user).order_by('-timestamp').first()
    
    if last_attendance:
        # Calculate the time difference between now and the last attendance timestamp
        time_difference = now() - last_attendance.timestamp
        # Check if the difference is greater than 24 hours
        if time_difference > timedelta(hours=24):
            alert_needed = True

    return render(request, 'home.html', {
        'user': user,
        'alert_needed': alert_needed,
    })

@login_required(login_url='/login/') 
def locationtrack(request):
    return render(request, 'location.html')


@login_required(login_url='/login/') 
def faceattendance(request):
    return render(request, 'Attendance.html')


def logout_view(request):
    logout(request)  # This will flush the session and invalidate the CSRF token
    return redirect('login')  # Redirect to the login page

@login_required(login_url='/login/')
def history(request):
    # Fetch attendance records for the logged-in user
    attendance_records = Attendance.objects.filter(student=request.user)
    # Pass the filtered records to the template
    return render(request, 'History.html', {'attendance_records': attendance_records})


@login_required(login_url='/login/') 
def profile(request):
    return render(request, 'Profile.html')


@login_required(login_url='/login/') 
def contact(request):
    return render(request, 'contact.html')
