from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import department, employee
from django.core import serializers
import json

# Create your views here.
def index(request):
    return render(request,"home.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # myuser= User.objects.create_user(username,email,password1)
        # myuser.save()
        # messages.success(request,"Your account is successfully created")
        # return redirect('/signin')


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            else:
                user = User(username, email, password1)
                print('user created')
                return redirect('/signin')
        else:
            messages.info(request, 'password not matching...')
            return redirect('/signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/registration')
            # username=user.username
            # return render(request,"home.html",{'username:username'})
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('/signin')

    return render(request, 'signin.html')

def registration(request):
    if request.method == "POST":

        return redirect('/getdata')
    return render(request,"registration.html")


def getdata(request):
    template_name = 'dropdown.html'
    deptcontext = department.objects.all()
    empcontext = employee.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username', False)
        email = request.POST.get('email',False)


        myuser = User(username=username, email=email)
        if myuser is not None:
            messages.success(request, "Your Application is submitted.")
            return redirect('/getdata')
        else:
            messages.error(request,'Invalid form submission.')
            messages.error(request,myuser.errors)
            return redirect('getdata')

    return render(request, template_name, {'department': deptcontext, 'employee': empcontext})


def branch(request):
    return render(request, 'branch.html')

def logout(request):
    return render(request,'logout.html')