from django.urls import path
from . import views


app_name = 'travelmap'

urlpatterns = [
    path('', views.travelmap,name='map'),
   
    
]
