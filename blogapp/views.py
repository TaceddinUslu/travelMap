from django.shortcuts import render
from blogapp.models import Blog


data = {
    "blogs": [
        {
            "id": 1,
            "title": "komple web geliştirme",
            "image": "iznik1.jpeg",
            "is_active": True,
            "is_home": False,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 2,    
            "title": "python kursu",
            "image": "iznik2.jpeg",
            "is_active": True,
            "is_home": True,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 3,
            "title": "django kursu",
            "image": "iznik3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "çok iyi bir kurs"
        }
    ]
}


def index(request):
    context = {
        'blogs': Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, "blogapp/index.html", context)

def blogs(request):
    context = {
        'blogs': Blog.objects.filter(is_active=True)
    }
    return render(request, "blogapp/blogs.html", context)

def blog_details(request, slug):
    
    blog =  Blog.objects.get(slug=slug)
    return render(request, "blogapp/blog_details.html",{
        "blog": blog
    })
