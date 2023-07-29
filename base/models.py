from django.db import models

# Create your models here.
class Glasses(models.Model):
    product_name  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='glasses')
    price = models.FloatField()

    def __str__(self) -> str:
        return self.product_name

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

def __str__(self) -> str:
        return self.title

class client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.TextField()
    image = models.ImageField(upload_to='clients')

    def __str__(self) -> str:
        return self.first_name + " "+ self.last_name