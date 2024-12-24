from django.shortcuts import render, get_object_or_404
from .models import Podcast, Article


def podcast_list(request):
    podcasts = Podcast.objects.all()
    articles = Article.objects.all()[:5]  
    return render(request, 'podcast/podcast_list.html', {'podcasts': podcasts, 'articles': articles})

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  
    return render(request, 'podcast/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'podcast/article_detail.html', {'article': article})

def contact_us(request):
    return render(request, 'podcast/contact_us.html')