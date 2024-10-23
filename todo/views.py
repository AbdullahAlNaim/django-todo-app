from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
# Create your views here.

class index(TemplateView):
    template_name = 'todo/index.html'
    task_form = TaskForm

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {
            'tasks': tasks
        })

    def post(self, request):
        form = self.task_form(request.POST)
        tasks = Task.objects.all()
        if form.is_valid():
            form.save()
            tasks = Task.objects.all()
            return render(request, self.template_name, {
                'tasks': tasks
            })

        return render(request, self.template_name, {
            'tasks': tasks
        })