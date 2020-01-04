from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogpost(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "blogapp_text": "Blog Page."
    }
    return render(request, 'blogapp.html', context)

def home(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "hometext": "Welcome Back."
    }
    return render(request, 'home.html', context)

def contact(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "contact_text": "Welcome to Our Contact Page."
    }
    return render(request, 'contact.html', context)

def about(request):
    #return HttpResponse("Welcome to Task Page")
    #return render(request, 'todolist.html', {})
    context = {
        "about_text": "Welcome to About Us."
    }
    return render(request, 'about.html', context)
    