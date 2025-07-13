from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=100, choices=[
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self) :
        return self.name 
