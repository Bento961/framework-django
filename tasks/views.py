from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/home.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description, user=request.user)
        return redirect('/')
    return render(request, 'tasks/create_task.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('/')
