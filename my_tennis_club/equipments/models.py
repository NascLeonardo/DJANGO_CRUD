from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
            return f"{self.name}"

