from django.db import models

# Create your models here.
class register(models.Model):
    objects = models.Manager()

    def __str__(self):
        return self.name

class Website(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Selldata(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

