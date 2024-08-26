from django.db import models

# Create your models here.

class Hardware(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name