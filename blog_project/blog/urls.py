from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('sort/<str:sorting>', PostListView.as_view() , name='blog-home'), # like filter
    path('category/<str:name>', PostListView.as_view(), name='blog-home'), # category filter
    path('user/<str:username>', UserPostListView.as_view(), name='user-blogs'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('like/<int:pk>', views.likeview, name='like_post'), # for like button
    path('dislike/<int:pk>', views.dislikeview, name='dislike_post'), # dislike button
]