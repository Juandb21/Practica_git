from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.urls import reverse

# Create your views here.
def index(request):
    db_data = Task.objects.all()    
    context = {
        'db_data': db_data[::-1]
        }
    
    return render(request, 'app/index.html', context)

def insert(request):
    if request.method == 'POST':
        task_title = request.POST.get('title', '')
        task_description = request.POST.get('description', '')
        if task_title:
            db_data = Task(title=task_title, description=task_description)
            db_data.save()
    return HttpResponseRedirect(reverse('app:index'))

def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task_title = request.POST.get('title', '')
        task_description = request.POST.get('description', '')
        if task_title:
            task.title = task_title
            task.description = task_description
            task.save()
            return HttpResponseRedirect(reverse('app:index'))

    context = {
        'task': task,
    }
    return render(request, 'app/update.html', context)

def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse('app:index'))