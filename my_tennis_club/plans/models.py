from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=90, null=True)


    def __str__ (self):
        return f"{self.title}"