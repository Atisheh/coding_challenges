from django.db import models


class One(models.Model):
    char = models.CharField(max_length=60)
    integ = models.IntegerField(default=0)
    boole = models.BooleanField(default=False)
