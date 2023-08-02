from django.shortcuts import render
from articles.models import Article

def articlelist(request):
    article = Article.object.all().order_by(datetime)
    return render (request, 'articles/articleslist.html',{'articles':article})



