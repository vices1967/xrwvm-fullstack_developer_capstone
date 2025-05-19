from django.db import models
# from django.utils.timezone import now  # ❌ No se usa, se elimina

# Model definitions
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="Car Make")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon")
    ]

    name = models.CharField(null=False, max_length=30, default="Car Model")
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPES, default=SEDAN)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.type}, {self.year})"

