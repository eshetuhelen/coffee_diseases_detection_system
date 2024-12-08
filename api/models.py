from django.db import models

class CoffeeLeafImage(models.Model):
    name = models.CharField(max_length=255, blank=True)  # Name of the image
    image = models.BinaryField()  # Store binary data
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"CoffeeLeafImage {self.id}"

