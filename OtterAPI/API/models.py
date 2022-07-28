from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Otter(models.Model):
    def __str__(self):
        return str(f"{self.name} ({self.sex}): {self.age} years old.")

    class Sex(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    name = models.CharField(max_length=12)
    sex = models.CharField(
        max_length=5,
        choices=Sex.choices,
        default=Sex.FEMALE,
    )
    age = models.SmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(25),
        ],
    )
