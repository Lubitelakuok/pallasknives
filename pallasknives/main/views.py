from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from .models import Video
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def project(request):
    video=Video.objects.all()
    return render(request, 'main/scene.html',{"video":video})

def application(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success_page.html')
    else:
        form = TaskForm()

    return render(request, 'main/application.html', {'form': form})

