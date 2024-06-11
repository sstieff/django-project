from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Invention(models.Model):
    name = models.CharField(max_length=255)
    inventor = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    background = models.TextField()
    outcome = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name