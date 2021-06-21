from django.urls import path
from . import views
urlpatterns = [
    path('', views.display),
    path('contact/', views.contact),
    path('about/', views.about),
    path('tech/', views.tech),
    path('android/', views.android),
]
