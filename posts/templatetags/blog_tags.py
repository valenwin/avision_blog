import markdown
from django import template
from django.conf import settings
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.filter(status='published').count()


@register.inclusion_tag('most_commented_posts.html')
def get_most_commented_posts_to(count=settings.COUNT_POSTS):
    most_commented_posts = Post.objects.filter(status='published').annotate(total_comments=Count('comments')) \
                               .order_by('-total_comments')[:count]
    return {'most_commented_posts': most_commented_posts}


@register.inclusion_tag('most_commented_posts.html')
def get_most_commented_posts_from(count=settings.COUNT_POSTS):
    most_commented_posts = Post.objects.filter(status='published').annotate(total_comments=Count('comments')) \
                               .order_by('-total_comments')[count:]
    return {'most_commented_posts': most_commented_posts}


@register.inclusion_tag('latest_posts.html')
def show_latest_posts_to(count=settings.COUNT_POSTS):
    latest_posts = Post.objects.filter(status='published') \
                       .order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('latest_posts.html')
def show_latest_posts_from(count=settings.COUNT_POSTS):
    latest_posts = Post.objects.filter(status='published') \
                       .order_by('-publish')[count:]
    return {'latest_posts': latest_posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
