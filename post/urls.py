from django.urls import path, include
from rest_framework.routers import \
    DefaultRouter
from .views import CategoryListView, \
    TagListView, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('tags/', TagListView.as_view()),
    path('', include(router.urls))

]

