from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination

from .permission import IsAuthorOrReadOnly

from .models import (
                    Category,
                    Tag,
                    Article,
                    SubArticle,
                    ArticleComment
                    )
from .serializers import (
                    CategorySerializer,
                    TagSerializer,
                    ArticleSerializer,
                    ArticlePOSTSerializer,
                    SubArticleSerializer,
                    ArticleCommentSerializer
                    )


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class ArticleAPIView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    serializer_post_class = ArticlePOSTSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        super().get_serializer_class()
        if self.request.method == 'GET':
            return self.serializer_class
        return self.serializer_post_class


class SubArticleAPIView(generics.ListCreateAPIView):
    # article/{article_id}/subarticle/
    queryset = SubArticle.objects.all()
    serializer_class = SubArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        qs = super().get_queryset()
        return qs.filter(article_id=article_id)

    def get_serializer_context(self, **kwargs):
        context = super().get_serializer_context()
        article_id = self.kwargs.get('article_id')
        context['article_id'] = article_id
        return context


class ArticleCommentAPIView(generics.ListCreateAPIView):
    # article/{article_id}/comment/
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        qs = qs.filter(article_id=article_id)
        return qs

    def get_serializer_context(self, **kwargs):
        context = super().get_serializer_context()
        article_id = self.kwargs.get('article_id')
        context['article_id'] = article_id
        return context




