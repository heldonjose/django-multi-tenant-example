from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
