from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['name', 'second_name', 'age', 'photo', 'date']
    list_filter = ['name']