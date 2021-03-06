from django.urls import path

from .feeds import LatestPostsFeed

from .views import PostListView, PostListUserView, PostDetailsView, PostListViewByCategory
from .views import PostCreateView, PostUpdateView, PostDeleteView
from .views import post_share, post_search, post_like, post_dislike

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/<str:author>/', PostListUserView.as_view(), name='posts_list_owner'),
    path('post/<str:slug>/', PostDetailsView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('post/<str:slug>/share/', post_share, name='share_post'),
    path('post/<str:slug>/like/', post_like, name="post_like"),
    path('post/<str:slug>/unlike/', post_dislike, name="post_dislike"),
    path('tag/<slug:tag_slug>/', PostListView.as_view(), name='posts_list_by_tag'),
    path('category/<str:category>/', PostListViewByCategory.as_view(), name='posts_list_by_category'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', post_search, name='post_search'),

]
