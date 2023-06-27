from django.contrib import admin
from .models import Category, Article, Comment

# Register your models here.
admin.site.register(Category)

class AdminArticle(admin.ModelAdmin):
    list_display=('title','category','add_time')

admin.site.register(Article, AdminArticle)

class AdminComment(admin.ModelAdmin):
    list_display=('article','email','comment','status')

admin.site.register(Comment, AdminComment)