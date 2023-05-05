from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"), 
    path("hello/<str:username>", views.hello , name="hello"),
    path("task/", views.task , name="task"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>", views.projectDetail, name="projectDetail"),
    path("createTask/", views.createTask, name="createTask"),
    path("createProject/", views.createProject, name="CreateProject"),
]
