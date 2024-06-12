
# Create your models here.
from django.db import models
class students(models.Model):
        name=models.CharField(max_length=50)
        college=models.CharField(max_length=100)
        course=models.CharField(max_length=30)
def __str__(self):
        return self.name1