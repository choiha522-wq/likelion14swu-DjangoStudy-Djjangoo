from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib import admin
from posts.models import Post, PostImage, Comment
import admin_thumbnails

@admin_thumbnails.thumbnail("photo")
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class InLineImageWidget(admin.StackedInline):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, "url", None):
            html = mark_safe(f'<img src="{value.url}" height="150">') + html
        return html

class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 1
    formfield_overrides = {
        models.ImageField: {
            'widget': InLineImageWidget,
        }
    }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInLine,
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]