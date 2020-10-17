from django.shortcuts import render

from django.core import serializers

from django.http.response import JsonResponse, HttpResponse

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    
    # JsonResponse로 응답하기
    # data = []
    
    # for article in articles:
    #     data.append(
    #         {
    #             'id': article.id,
    #             'title': article.title,
    #             'content': article.content,
    #         }
    #     )
        
    # return JsonResponse(data, safe=False)
    
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
