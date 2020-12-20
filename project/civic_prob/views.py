from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django import template
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import random,datetime
from .models import MyProfile,Posts,comments
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
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
    #q_set=Posts.objects.all()
    return render(request,"files/viewposts.html")
    

def displaymyposts(request):
    #q_set=Posts.objects.filter(profile=request.user)
    return render(request,'files/viewprofile.html')


def upload(request):
    if request.method=='POST':
        img=request.POST['img']
        title=request.POST['title']
        decr=request.POST['description']
        ins=Posts(image=img,title=title,description=desc,date=datetime.datetime.today(),time=datetime.datetime.now())
        ins.save()
    else:
        return render(request, 'files/createisuue.html')

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return render(request, 'files/login.html')