from django.db import models


class News(models.Model):
    """News data model."""
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=200)
    url = models.CharField(null=False, blank=False, max_length=200)
    created = models.DateTimeField(auto_now=True)

