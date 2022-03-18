from django.shortcuts import render
from rest_framework import generics
from . import serializers
from .models import News


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
