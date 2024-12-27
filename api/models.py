from django.db import models

class CoffeeLeafImage(models.Model):
    image = models.ImageField(upload_to='coffee_leaf_images/')
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.label} - {self.image.name}"
