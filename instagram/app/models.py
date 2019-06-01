from django.db import models

# Create your models here.
class Employee(models.Model):
    """
    Employee talble
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        represents the record
        """
        return self.name