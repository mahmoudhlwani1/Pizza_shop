from django.db import models
class Pizza(models.Model):
 name = models.CharField(max_length=100)
 size = models.CharField(max_length=1, choices=SIZE_CHOICES)
price = models.DecimalField(max_digits=5, decimal_places=2)
def __str__(self):
 {
 return self.name;
 }	


# Create your models here.
