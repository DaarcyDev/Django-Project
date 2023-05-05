from django import forms

class CreateNewTask (forms.Form):
    title = forms.CharField(label="Title Task",  max_length= 200)
    description =forms.CharField(label="Description Task", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project Name", max_length= 200)