from django.shortcuts import render, render, redirect, get_object_or_404
import requests
import json

# Create your views here.
def index(request):
    response = requests.get('http://127.0.0.1:8000/api/category/')
    new = requests.get('http://127.0.0.1:8000/api/listjobs/')

    context = {
        'response': response.json(),
        'new': new.json()
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def jobs(request):
    response = requests.get('http://127.0.0.1:8000/api/category/')
    new = requests.get('http://127.0.0.1:8000/api/listjobs/')

    context = {
        'response': response.json(),
        'new': new.json()
    }

    return render(request, 'jobs.html', context)

def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')

def blog(request):
    return render(request, 'blog.html')

def employer_postdash(request):
    return render(request, 'employer_postdash.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def post_details(request):
    return render(request, 'post_details.html')