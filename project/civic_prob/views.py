from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django import template
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def home(request):
    return render(request, 'files/home.html')

def login(request):
    global loggedin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        global_dict['email'] = username
        if user is not None:
            auth.login(request, user)
            loggedin = True
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('home')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username'] or None
        password = request.POST['password']
        password1 = request.POST['confrom_password']
        if len(password) < 8:
            messages.info(
                request, "Password should be minimum of 8 charachters")
            return redirect('home')
        if password == email:
            messages.info(request, "Password should not be same as email")
            return redirect('home')
        if password == password1:
            try:
                User.objects.get(username=username)
                messages.info(
                    request, "There's already an account with this email")
                return redirect('signup')
            except:
                user = User.objects.create_user(
                    username=email, password=password)
                userobj=MyProfile(user=user)
                userobj.save()
            auth.login(request, user)
            # email sending

            return redirect('viewPosts')
        else:
            messages.info(
                request, "Password and Confirm Password should match")
            return redirect('home')