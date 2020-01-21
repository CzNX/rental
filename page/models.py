from django.db import models

# Create your models here.
class Rental(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to='pics')
  desc = models.TextField()
  price = models.IntegerField()
  dt = models.DateTimeField()


  def __str__(self):
    return self.name