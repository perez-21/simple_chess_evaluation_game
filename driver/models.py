from django.db import models

# Create your models here.
class Position(models.Model):
  fen = models.CharField(max_length=200)
  evaluation = models.IntegerField()