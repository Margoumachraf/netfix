# services/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Company


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hour = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    field = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
