from django.shortcuts import render, redirect
from articles.models import Article, Category, Comment


# Create your views here.
def Article_view(request):
    
    context = {}
    articles = Article.objects.all()
    context['articles'] = articles
    
    #return redirect('homepage')
    
    
    return render(request, 'articles/article.html', context)
