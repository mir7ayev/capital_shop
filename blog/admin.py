from django.contrib import admin
from .models import (
    PostTag, Post, Comment,
)


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
