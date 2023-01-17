from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Category, Tag, Post, Comment
from .permission import IsAdminAuthPermission,\
    IsAuthorPermission
from .serializers import CategorySerializer, \
    TagSerializer, PostSerializer, PostListSerializer, CommentSerializer
import django_filters
from rest_framework import filters


class CategoryListView(
    generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class PostListCreateView(
#     generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['category']
#     search_fields = ['tags__slug', 'created_at']
#
# class PostDetailView(
#     generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['tags__slug', 'created_at']
    ordering_fields = ['created_at', 'title']

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [
                IsAdminAuthPermission]
        elif self.action in ['update',
                    'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]

        return super().get_permissions()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [
                IsAdminAuthPermission]
        elif self.action in ['update',
                    'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]

        return super().get_permissions()
