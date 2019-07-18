from django.db import models
from datetime import datetime

# Create your models here.
class Container(models.Model):
    number  = models.CharField(max_length=11)
    carrier = models.CharField(max_length=128)
    status = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    last_import = models.DateTimeField(default=datetime.now)