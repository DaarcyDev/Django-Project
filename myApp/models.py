from django.db import models

# Create your models here.
class Projects(models.Model ):
    name = models.CharField(max_length=200)

    #para ver los nombres de los proyectos en la aplicacion de django
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    Done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + self.project.name