from rest_framework import serializers

from app.account.serializers import UserSerializer
from .models import (
                    Category,
                    Tag,
                    Article,
                    SubArticle,
                    ArticleComment
                    )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'tags', 'category', 'slug', 'image', 'content', 'created_date']
        red_only = ['created_date']


class ArticlePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'tags', 'category', 'slug', 'image', 'content', 'created_date']
        red_only = ['created_date']

    def create(self, validated_data):
        request = self.context['request']
        author_id = request.user.id
        validated_data['author_id'] = author_id
        return super().create(validated_data)


class SubArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArticle
        fields = ['id', 'title', 'image', 'content']

    def create(self, validated_data):
        article_id = self.context.get('article_id')
        validated_data['article_id'] = article_id
        return super().create(validated_data)


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ['id', 'parent', 'top_level_comment_id', 'message', 'created_date']
        red_only_field = ['created_date', 'top_level_comment_id']

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context.get('article_id')
        author_id = request.user.id
        validated_data['article_id'] = article_id
        validated_data['author_id'] = author_id
        return super().create(validated_data)
