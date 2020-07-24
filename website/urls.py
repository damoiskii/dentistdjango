from django.urls import path
from . import views

# Normally I would use the path('contact/', views.contact, name='contact') way of linking...
# But this path('contact.html', views.contact, name='contact') way of doing it makes it a bit easier since I imported
# ready done template...
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('appointment/', views.appointment, name='appointment'),
]
