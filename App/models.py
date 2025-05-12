from django.db import models

# Create your models here.
class Data(models.Model):
    end_year = models.IntegerField()
    intensity = models.IntegerField()
    sector = models.CharField(max_length=256)
    topic = models.CharField(max_length=256)
    insight = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    region = models.CharField(max_length=256)
    start_year = models.IntegerField()
    impact = models.IntegerField()
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=256)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
    title = models.CharField(max_length=1024)
    likelihood = models.IntegerField()