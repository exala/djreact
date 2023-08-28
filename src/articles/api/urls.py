from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleSearchAPIView
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', ArticleSearchAPIView.as_view())
]