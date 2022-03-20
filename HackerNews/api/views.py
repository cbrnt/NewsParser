from .serializers import NewsSerializer
from .models import News
from rest_framework import viewsets
from rest_framework import filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title']
