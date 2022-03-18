from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.NewsList.as_view()),
    path('posts/<int:pk>/', views.NewsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
