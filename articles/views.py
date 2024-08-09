# articles/views.py
from rest_framework import viewsets
from .models import Article, CustomUser
from .serializers import ArticleSerializer, UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

