from django.contrib import admin
from articles.models import Article, Category, Comment

admin.site.register(Article)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
