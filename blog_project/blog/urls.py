from django.urls import path,include
from .views import (
    home, 
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

app_name = 'blog'
urlpatterns = [
    path('',PostListView.as_view(),name="home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new',PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="post-update"),
    path('user/<str:username>',UserPostListView.as_view(),name="user-post"),   
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name="post-delete"),   
]