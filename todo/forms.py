from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'task_name': 'task',
            'complete': 'done'
        }