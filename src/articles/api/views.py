from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter

from articles.models import Article
from .serializers import ArticleSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleSearchAPIView(ListCreateAPIView):
    search_fields = ['title', 'content']
    filter_backends = (SearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer