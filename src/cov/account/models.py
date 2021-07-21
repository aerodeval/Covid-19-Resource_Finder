from django.db import models

# Create your models here.
class newpro(models.Model):
    description=models.TextField()

    Product = models.CharField(max_length=100)
    contactno=models.CharField(max_length=100)
