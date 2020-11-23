from django.urls import path
from . import views

urlpatterns = [
    path('xss', views.jv, name='xss'),
]