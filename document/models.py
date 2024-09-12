from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()

class AttrTemplate(models.Model):
    key = models.CharField(max_length=50)
    ru_key = models.CharField(max_length=50)
    template = models.ForeignKey('Template', on_delete=models.CASCADE)
    
# Create your models here.
