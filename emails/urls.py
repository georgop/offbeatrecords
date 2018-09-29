from django.urls import path
from . import views
from .models import info

urlpatterns= [
    path('',views.new,name='home'), 
]