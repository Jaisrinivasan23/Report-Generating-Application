from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, FacultyForm
from .models import Faculty

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = '123'

def homepage_view(request):
    return redirect('admin_login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
           
            return redirect('admin_home')
        else:    
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html', {'role': 'Admin'})

def admin_home(request):
    return render(request, 'admin_home.html')

def add_faculty_view(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty added successfully.')
            return redirect('add_faculty')
        else:
            messages.error(request, 'Invalid form data. Please try again.')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

def academic_performance_view(request):
    return render(request, 'academic_performance.html')

def research_publications_view(request):
    return render(request, 'research_publications.html')

def financial_statements_view(request):
    return render(request, 'financial_statements.html')

def infrastructure_developments_view(request):
    return render(request, 'infrastructure_developments.html')

def student_faculty_achievements_view(request):
    return render(request, 'student_faculty_achievements.html')

def extracurricular_activities_view(request):
    return render(request, 'extracurricular_activities.html')
