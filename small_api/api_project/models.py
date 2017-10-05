from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=60)
    # aka country to make it a bit more unique and with less options
    location = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
