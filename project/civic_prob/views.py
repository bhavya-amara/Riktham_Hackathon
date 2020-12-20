from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django import template
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import random
from .models import MyProfile,Posts,comments
# Create your views here.

def login(request):
    global loggedin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            loggedin = True
            #return HttpResponse("logged successfully")
            return redirect('viewposts')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "files/login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username'] or None
        password = request.POST['password']
        password1 = request.POST['conform_password']
        if len(password) < 8:
            messages.info(
                request, "Password should be minimum of 8 charachters")
            return redirect('signup')
        if password == username:
            messages.info(request, "Password should not be same as email")
            return redirect('signup')
        if password == password1:
            try:
                User.objects.get(username=username)
                messages.info(request, "There's already an account with this email")
                return redirect('signup')
            except:
                user = User.objects.create_user(username=username, password=password)
                userobj=MyProfile(user=user)
                userobj.save()
                auth.login(request, user)
            # email sending

            return redirect('viewposts')
        else:
            messages.info(request, "Password and Conform Password should match")
            return redirect('signup')
    else:
        return render(request, "files/signup.html")
    
def displayposts(request):
    q_set=Posts.objects.all()
    return render(request,"files/viewposts.html",{'posts':q_set.values()})
    

def displaymyposts(request):
    q_set=Posts.objects.filter(profile=request.user)
    return render(request,'files/viewprofile.html',{'posts':q_set})


def upload(request):
    if request.method=='POST':
        pass
    else:
        return render(request, 'files/createisuue.html')