from todolist import views
from django.urls import path
#from templates.css import todolist


urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('home', views.home, name='home_td'),
    path('todo_contact', views.contact, name='contact_td'),
    path('todo_about', views.about, name='about_td')
]

 