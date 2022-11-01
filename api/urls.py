
from django.views.generic import base
from likes.views import LikeViewSet
from posts.views import PostViewSet,AddPostViewSet
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import ProfileViewSet

router = DefaultRouter()

urlpatterns=[
    
    
]

router.register(r'users', UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet)
router.register(r'posts',PostViewSet,basename='posts')
router.register(r'addpost',AddPostViewSet)
router.register(r'likes',LikeViewSet)
urlpatterns=urlpatterns+router.urls