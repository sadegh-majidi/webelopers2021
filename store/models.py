from django.contrib.auth.models import User
from django.db import models


class ContactRequest(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=80)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class Seller(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
