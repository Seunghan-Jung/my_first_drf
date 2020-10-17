from django.shortcuts import render

from django.http.response import JsonResponse

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    
    data = []
    
    for article in articles:
        data.append(
            {
                'id': article.id,
                'title': article.title,
                'content': article.content,
            }
        )
        
    return JsonResponse(data, safe=False)
