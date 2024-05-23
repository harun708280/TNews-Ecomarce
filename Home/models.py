

# Create your models here.
from django.db import models

# Create your models here.

class Cetagory(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
    
class Sub_cetagory(models.Model):
    cetagory=models.ForeignKey(Cetagory,verbose_name='Main Cetagory', on_delete=models.CASCADE)
    name=models.CharField(verbose_name='Sub Cetagory', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Sub Cetagory'
        
        
        
class NavImage(models.Model):
    image=models.ImageField(upload_to='Nav Images', )
    
    def __str__(self):
        return str(self.id)
    