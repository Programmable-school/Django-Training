from django.db import models

class Page(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=256)
  description = models.CharField(max_length=1024)
  href = models.URLField(max_length=2084)
  date_published = models.DateField()

class Feed(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=256)
  description = models.CharField(max_length=1024)
  href = models.URLField(max_length=2084)
  rss = models.URLField(max_length=2084)