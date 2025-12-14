from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author_username')
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'author_name', 'created_at', 'updated_at']
        
        def create(self, validated_data):
            return super().create(validated_data)
        
class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments']
    read_only_fields = ['id', 'author', 'author_username', 'created_at', 'updated_at', 'comments']