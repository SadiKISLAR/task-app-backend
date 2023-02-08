from django.db import models

# Create your models here.

class Test(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    sector=models.CharField(max_length=100)
    agree_to_terms=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name