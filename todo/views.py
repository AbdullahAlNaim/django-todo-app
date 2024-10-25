from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import CreateView

# Create your views here.

class IndexView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/index.html'
    success_url = '/created'

class CreatedView(TemplateView):
    template_name = 'todo/task_created.html'