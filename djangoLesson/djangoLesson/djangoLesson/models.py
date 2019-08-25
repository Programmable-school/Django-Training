from django.db import models
from django.utils import timezone

class Diary(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=256)
  content = models.CharField(max_length=65536)
  date_published = models.DateTimeField(default=timezone.now)