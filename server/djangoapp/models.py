
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    founded = models.IntegerField()
    website = models.URLField(max_length=200)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('PICKUP', 'Pickup'),
        ('COUPE', 'Coupe'),
        ('VAN', 'Van'),
        ('MOTORCYCLE', 'Motorcycle'),
        ('OTHER', 'Other'),
        # Add more choices as required
    ]
    Fuel_Types = [
        ('GASOLINE', 'Gasoline'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid'),
        ('OTHER', 'Other'),
    ]
    type = models.CharField(max_length=100, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    fuel_type = models.CharField(max_length=10, choices=Fuel_Types, default='GASOLINE')
    # Other fields as needed
    mileage = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    color = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    doors = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)
    def __str__(self):
        return self.name  # Return the name as the string representation
