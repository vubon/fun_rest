"""User model"""
from django.db import models


class Tags(models.Model):
    """User tag atrribute"""
    name = models.TextField(max_length=300)
    expiry = models.PositiveIntegerField()


# Create your models here.
class User(models.Model):
    """User model atrribute"""
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}"
