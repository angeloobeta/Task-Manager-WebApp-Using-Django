from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Todolist
from todolist.forms import TodoForms
from django.contrib import messages


# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TodoForms(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task"))
        return redirect('todolist')

    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})

    else:
        all_tasks = Todolist.objects.all
        return render(request, 'todolist.html', {'all_tasks':all_tasks})
    
    # context = {
    #     "welcome_text": "Welcome to Task Page.",
    # }
    # return render(request, 'todolist.html', context)

def delete_task(request, task_id):
    task = Todolist.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')


def edit_task(request, task_id):
    if request.method == "POST":
        task = Todolist.objects.get(pk=task_id)
        form = TodoForms(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited"))
        return redirect('todolist')

    else:
        task_obj = Todolist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})
    
def home(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "home_text": "Welcome Back.",
    }
    return render(request, 'home.html', context)

def contact(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "contact_text": "Welcome to Our Contact Page.",
    }
    return render(request, 'contact.html', context)
    
def about(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "about_text": "Welcome to About Us.",
    }
    return render(request, 'about.html', context)
    