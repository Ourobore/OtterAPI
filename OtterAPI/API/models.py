from django.db import models

# Create your models here.
class Otter(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=12)
