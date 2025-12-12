from django.db import models
from django.conf  import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like, Notification

User = get_user_model()
User = settings.AUTH_USER_MODEL


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "Already liked."}, status=400)
        
        if post.author != request.user:
            Notification.objects.create(
                user=post.author,
                message=f"{request.user.username} liked your post.",
                post=post
            )
        return Response({"detail": "Post liked successfully."})


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked successfully."})
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=400)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(default="")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
class Meta:
    ordering = ['-created_at']
    
def __str__(self):
    return f"{self.title} by {self.author.username}"


class Like(models.Model):
    post = models.ForeignKey('posts.post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('post', 'user')
        ordering = ['-timestamp']
        
    def __str__(self):
        return f"{self.user} -> {self.post_id}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    contents = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f"Comment by{self.author.username} on {self.post.id}"
    

