from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

def blog(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'Articles': articles })

def blog_page(request, page_id):
    article = models.Article.objects.get(pk=page_id)
    return render(request, 'blog/blog_page.html', {'Article': article })

def edit_page(request):
    return render(request, 'blog/editor.html')

def sub_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    return HttpResponseRedirect('index')