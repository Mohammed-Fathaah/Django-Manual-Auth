from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.TextField()
    email=models.EmailField()
    password=models.TextField()

    def __str__(self):
        return self.name