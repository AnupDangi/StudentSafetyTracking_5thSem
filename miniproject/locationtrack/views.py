from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def getstarted(request):

    return render(request,'getstarted.html',)


def login(request):

    return render(request,'login.html',)


# Note : We use httpresponse only when we dont have any other file we are returning a block of message it cannot render a whole wepage 


def signup(request):

    return render(request,'signup.html')

def login(request):

    return render(request,'login.html')

def home(request):
    #return HttpResponse('This is services page')
    return render(request,'home.html')



# features

def locationtrack(request):
    return render(request,'location.html')
    # return HttpResponse('This is contact page')


def faceattendance(request):
    return render(request,'Attendance.html')
    # return HttpResponse('This is contact page')

def history(request):
    return render(request,'History.html')
    # return HttpResponse('This is contact page')


def Profile(request):
    return render(request,'Profile.html')
    # return HttpResponse('This is contact page')


def contact(request):
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')




