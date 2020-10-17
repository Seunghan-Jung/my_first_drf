# My First DRF

django 서버를 이용해 요청에 JSON으로 응답하는 API 서버를 만들어보자

## A. JsonResponse

첫 번째 방법은 `JsonResponse` 객체를 이용하는 것이다.

- 모델

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=50)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return self.title
  ```

- 뷰

  - `JsonResponse`를 사용하기 위해서 import

    ```python
    from django.http.response import JsonResponse
    ```

  - `JsonResponse`에 인자로 넘길 `data`는 딕셔너리 타입이어야 한다.

    ```python
    def index(request):
        articles = Article.objects.all()
        
        data = {
            'articles': [],
        }
        
        for article in articles:
            data['articles'].append(
                {
                    'id': article.id,
                    'title': article.title,
                    'content': article.content,
                }
            )
            
        return JsonResponse(data)
    ```

  - 응답

    ```json
    {
        "articles": [
            {
                "id": 1,
                "title": "System seat physical two.",
                "content": "Indicate fine painting student purpose.\nRadio child would medical after seek. Concern need strong eight nice big.\nTechnology rock feel loss foot. Film military yourself build."
            },
            {
                "id": 2,
                "title": "Bar turn tonight media.",
                "content": "Nor sing very leave take. Report people sea ball far either hot effort. Very section itself hand billion us such. All couple control growth writer.\nMedia Democrat newspaper or seven."
            }
    }
    ```

  - 만일 딕셔너리가 아닌 타입으로 응답하고자 한다면 `safe=False` 옵션을 준다.

    ```python
    def index(request):
        articles = Article.objects.all()
        
        # 리스트 타입
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
    ```

  - 응답

    ```json
    [
        {
            "id": 1,
            "title": "System seat physical two.",
            "content": "Indicate fine painting student purpose.\nRadio child would medical after seek. Concern need strong eight nice big.\nTechnology rock feel loss foot. Film military yourself build."
        },
        {
            "id": 2,
            "title": "Bar turn tonight media.",
            "content": "Nor sing very leave take. Report people sea ball far either hot effort. Very section itself hand billion us such. All couple control growth writer.\nMedia Democrat newspaper or seven."
        }
    ]
    ```

- 문제점

  - 필드를 일일이 적어주며 딕셔너리를 만들어야 하는 것이 불편하다

## B. 