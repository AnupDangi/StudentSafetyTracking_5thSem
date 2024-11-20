from django.contrib import admin
from django.urls import path
from locationtrack import views
admin.site.site_header = "Purnima Suppliers"
admin.site.site_title = "Welcome"
admin.site.index_title = "Shop With US"

urlpatterns = [
    path("", views.getstarted, name="getstarted"),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path("login",views.login,name='login'),
    path("home",views.home,name='home'),
    path("faceattendance",views.faceattendance,name='faceattendance'),
    path("contact",views.contact,name='contact'),
    path("history",views.history,name='history'),
    path("location",views.locationtrack,name='location-track'),
    path("Profile",views.Profile,name='Profile'),

]