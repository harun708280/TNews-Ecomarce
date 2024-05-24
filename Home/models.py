from django.contrib.auth.models import User

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

class Add_News(models.Model):
    cetagory=models.ForeignKey(Cetagory, verbose_name=("Add To Cetagory"), on_delete=models.CASCADE,blank=True,null=True)
    sub_cetagory=models.ForeignKey(Sub_cetagory, verbose_name=("Sub Cetagory"), on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField( max_length=150,blank=True,null=True)
    Create=models.CharField(default='T-News', max_length=50,blank=True,null=True)
    descripton=models.TextField(blank=True,null=True)
    image=models.ImageField( upload_to='News Image',blank=True,null=True )
    vedio=models.FileField( upload_to='Vedeos/',blank=True,null=True)
    like=models.ManyToManyField(User, blank=True,null=True)
    total_views = models.IntegerField(default=0,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name=("Add to News")