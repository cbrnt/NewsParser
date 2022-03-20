from .serializers import NewsSerializer
from .models import News
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
