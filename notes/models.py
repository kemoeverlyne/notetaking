from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)    
    
    def __str__(self):
        return self.name
      


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title
    
# Create your models here.
