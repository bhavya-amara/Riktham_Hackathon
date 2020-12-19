from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.
def home(request):
    return render(request, 'files/home.html')

def login(request):
    return render(request,"files/login.html")


def signup(request):
    return render(request, "files/signup.html")