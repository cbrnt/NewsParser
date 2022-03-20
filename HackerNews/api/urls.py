from rest_framework import routers
from .views import NewsViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'posts', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include('rest_framework.urls', namespace='rest_framework')),
]
