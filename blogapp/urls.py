from django.urls import path
from . import views


app_name = 'blogapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs", views.blogs, name="blogs"),
    path('blogs/<slug:slug>/', views.blog_details, name='blog_details'),
]
