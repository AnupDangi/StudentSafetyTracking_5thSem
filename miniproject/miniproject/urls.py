from django.contrib import admin
from django.urls import path
from locationtrack import views


urlpatterns = [
    path('', views.getstarted, name='getstarted'),
    path('login/', views.custom_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('is_face_registered/', views.is_face_registered, name='is_face_registered'),
    path('location/', views.locationtrack, name='locationtrack'),
    path('faceattendance/', views.faceattendance, name='faceattendance'),
    path('history/', views.history, name='history'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('add_user_face/', views.add_user_face, name='add_user_face'),
    path('verify_attendance/', views.verify_attendance, name='verify_attendance'),
    path('record_attendance/', views.record_attendance, name='record_attendance'),

    #path('validate_location/', views. check_location_valid, name='validate_location'),
   
    path('admin/', admin.site.urls)
]