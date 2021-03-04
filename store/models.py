from django.db import models


class ContactRequest(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.CharField(max_length=250)
