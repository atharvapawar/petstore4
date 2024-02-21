from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)

    def __str__(self):
        return f"{ self.name }"