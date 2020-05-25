from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    print(request.POST)
    errors = Course.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    new_course = Course.objects.create(course_name = request.POST['name'], description = request.POST['desc'])
    print(new_course, "New course has been added!")
    request.session['name'] = new_course.name
    request.session['id'] = new_course.id
    return render(request, 'index.html')

def add(request):
    return render(request, '/')