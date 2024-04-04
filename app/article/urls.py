from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
                CategoryAPIView,
                TagAPIView,
                ArticleAPIView,
                SubArticleAPIView,
                ArticleCommentAPIView
                    )

router = DefaultRouter()

router.register('article', ArticleAPIView)

app_name = 'article'


urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('tag/', TagAPIView.as_view(), name='tag'),
    path('<int:article_id>/comment/', ArticleCommentAPIView.as_view(), name='comment'),
    path('<int:article_id>/subarticle/', SubArticleAPIView.as_view(), name='subarticle'),
    path('', include(router.urls))

]


"""
    Category
        - list
        
    Tag
        -list
        
    Article
        -list
        -detail
        -create
        -update
        -delete
    
    SubArticle
        -list
        -create
        -delete
    
    ArticleComment
        -list
        -create
"""