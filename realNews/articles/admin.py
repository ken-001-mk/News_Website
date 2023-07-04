from django.contrib import admin
from articles.models import Article, Category, Comment

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'id')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author', 'id')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')