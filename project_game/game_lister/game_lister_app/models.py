from django.db import models

# Create your models here.
class Gamer(models.Model):
  title = models.CharField(max_length=100)
  platform = models.CharField(max_length=100)
  score = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  editors_choice = models.CharField(max_length=10)
  
  
  def __str__(self):
    return self.title

