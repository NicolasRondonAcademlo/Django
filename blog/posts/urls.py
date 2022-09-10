from django.urls import path
from .views import PostList, PostDetail, PostViewSet, UserDetail, UserList
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
urlpatterns = [
    path("users/", UserList.as_view()), # new
    path("users/<int:pk>/", UserDetail.as_view()), 
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
] + router.urls