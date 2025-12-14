
from django.urls import path
from .views import (
    PostViewSet,
    CommentViewSet,
    FeedView,
    LikePostView,
    UnlikePostView,
)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:post_id>/', LikePostView.as_view(), name='like-post'),
    path('unlike/<int:post_id>/', UnlikePostView.as_view(), name='unlike-post'),
]
