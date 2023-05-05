from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Projects,Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "Welcome to django Course" 
    return render(request, "index.html", {
        'title':title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</ h2>" %username)

def about(request):
    username = "Daarcyy"

    return render(request, "about.html",{
        "username":username 
    })

def projects(request):
    # projects = list(Projects.objects.values())
    projects = Projects.objects.all()
    return render(request, 'projects/projects.html', {
        "projects":projects 
    })

def task(request):
    task = Task.objects.all()
    return render(request, 'tasks/task.html',{
        'tasks':task
    })
def createTask(request):

    if(request.method == 'GET'):
        return render(request, "tasks/createTask.html",{
            "forms" : CreateNewTask()
        })
    else:
        task = Task.objects.create(title = request.POST['title'],description = request.POST['description'],project_id =1)
        return redirect('task') 
        
def createProject(request):

    if(request.method == 'GET'):
        return render(request, "projects/createProject.html",{
            "forms" : CreateNewProject()
        })
    else:
        project = Projects.objects.create(name = request.POST['name'])
        return redirect('projects') 
        
def projectDetail(request, id):
    print(id)
    # project = Projects.objects.get(id=id)
    project = get_object_or_404(Projects,id=id)
    task = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        "project": project,
        "tasks": task
    })