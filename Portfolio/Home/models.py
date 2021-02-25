from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phone = models.IntegerField()
    addr = models.TextField()
    def __str__(self):
        return self.fullName
    
