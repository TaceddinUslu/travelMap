from django.contrib import admin
from .models import Blog, Category

class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "slug")
    list_editable = ("is_active", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)

class Categoryadmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    readonly_fields = ("slug",)
    
    





admin.site.register(Blog, Blogadmin)
admin.site.register(Category,Categoryadmin)   


