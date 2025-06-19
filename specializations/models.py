from django.db import models

# Create your models here.
class Specializations(models.Model):
    specialization_name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=100, unique=True)

def __str__(self):
    return self.specialization_name
