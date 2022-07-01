from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Project,Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','status','admin_todo')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','status','text_todo','end_date','project')