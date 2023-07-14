from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # Add other fields like address, cuisine type, etc. as per your requirements

    def __str__(self):
        return self.name


