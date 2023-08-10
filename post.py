from rest_framework import serializers
from django_blog.apps.account.models import User
from django_blog.apps.blog.models import Tag, Post
class UserSerializer(serializers.ModelSerializer):
class Meta:
model = User
fields = ('pk', 'email', 'first_name', 'last_name',)
class TagSerializer(serializers.ModelSerializer):
class Meta:
model = Tag
fields = ('pk', 'name',)
class PostSerializer(serializers.ModelSerializer):
tags = TagSerializer(many=True, required=False, read_only=True)
author = UserSerializer(required=False, read_only=True)
serializers.ImageField(use_url=True, required=False, allow_null=True)
class Meta:
model = Post
fields = ('pk', 'title', 'text', 'tags', 'author', 'image',)
from django_blog.apps.blog.models import Post
from django_blog.apps.blog.rest_api.serializers.post import PostSerializer
post = Post.objects.create(title='First post', text='This is a first post')
print(PostSerializer(post).data)
# {'pk': '4670511f-4a03-455e-a160-18c396fa743d', 'title': 'First post', 'text': 'This is a first post', 'tags': [], 'author': None, 'image': None}
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_blog.apps.blog.models import Post
from django_blog.apps.blog.rest_api.serializers.post import PostSerializer
class PostListCreateAPIView(ListCreateAPIView):
"""
    API view to retrieve list of posts or create new
    """
serializer_class = PostSerializer
queryset = Post.objects.active()
class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
"""
    API view to retrieve, update or delete post
    """
serializer_class = PostSerializer
queryset = Post.objects.active()
