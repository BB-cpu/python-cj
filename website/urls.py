from django.urls import path
from . import views
urlpatterns = [
    path('home.html', views.home, name="home.html"),
    path('contact.html', views.contact, name="contact.html"),
    path('about.html', views.about, name="about.html"),
    path('doctors.html', views.doctors, name="doctors.html"),
    path('news.html', views.news, name="news.html"),
    path('services.html', views.services, name="services.html"),
    ]