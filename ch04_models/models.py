from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, # allow empty category
        related_name='posts',
        )