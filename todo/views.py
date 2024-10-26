from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views import View

# Create your views here.

class IndexView(View):
    template_name = 'todo/index.html'
    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, self.template_name, {
            'tasks': tasks,
            'form': form
        })

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        tasks = Task.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'tasks': tasks
        })
    # model = Task
    # form_class = TaskForm
    # template_name = 'todo/index.html'
    # success_url = '/created'

class CreatedView(TemplateView):
    template_name = 'todo/task_created.html'