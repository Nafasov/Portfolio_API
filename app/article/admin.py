from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    Tag,
    Article,
    SubArticle,
    ArticleComment
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class SubArticleAdmin(admin.TabularInline):
    model = SubArticle
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SubArticleAdmin]
    list_display = ('id', 'title', 'author', 'created_date')
    search_fields = ('title', )
    readonly_fields = ('created_date', 'modified_date', 'slug')
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'article', 'top_level_comment_id', 'created_date')

