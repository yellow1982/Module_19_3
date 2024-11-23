from django.db import models



class Buyer(models.Model):

    name = models.CharField(max_length=30, )
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField(max_length=3)

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')



