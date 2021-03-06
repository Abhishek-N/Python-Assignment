from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField()
