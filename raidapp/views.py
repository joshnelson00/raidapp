from django.db import connection
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")
