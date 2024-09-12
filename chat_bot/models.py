from django.db import models


class QueryAnswer(models.Model):
    query = models.TextField()
    
    answer = models.TextField()
# Create your models here.
