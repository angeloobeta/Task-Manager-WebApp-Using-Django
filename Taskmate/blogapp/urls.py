from blogapp import views
from django.urls import path

urlpatterns = [
    path('', views.blogpost, name='blogapp'),
    path('home', views.home, name='home_ap'),
    path('about', views.about, name='about_ap'),
    path('contact', views.contact, name='contact_ap')

]

