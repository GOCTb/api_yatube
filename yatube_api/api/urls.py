from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from .views import PostViewSet, GroupViewSet, CommentViewSet

# Основной роутер для постов и групп
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

# Отдельный роутер для комментариев, который будет вложен в URL поста
comment_router = DefaultRouter()
comment_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Эндпоинт получения токена
    path('api-token-auth/', token_views.obtain_auth_token),
    # Все маршруты из основного роутера (api/v1/posts/, api/v1/groups/ и т.д.)
    path('', include(router.urls)),
    # Вложенные маршруты: api/v1/posts/<post_id>/comments/ и api/v1/posts/<post_id>/comments/<comment_id>/
    path('posts/<int:post_id>/', include(comment_router.urls)),
]