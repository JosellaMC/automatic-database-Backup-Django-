from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    