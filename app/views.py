from django.shortcuts import render
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

def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse('app:index'))