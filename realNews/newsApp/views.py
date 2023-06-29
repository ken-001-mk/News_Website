from django.shortcuts import render
from articles.models import Article
from account.models import Account

# Create your views here.
def homepage(request):
    
    context = {}
    articles = Article.objects.all()
    context['articles'] = articles
    
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    return render(request, 'newsApp/home.html', context)
