from django.contrib import admin

from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'author', 'slug', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    list_per_page = 20


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'body')
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title',)
    list_per_page = 15
