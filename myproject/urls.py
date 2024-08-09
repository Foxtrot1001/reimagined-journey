from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from articles import views  # Исправьте импорт здесь

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
