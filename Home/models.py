from django.contrib.auth.models import User
from autoslug import AutoSlugField
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
    date=models.DateField( auto_now_add=True,blank=True,null=True)
    
    news_slug = AutoSlugField(populate_from='title', unique=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name=("Add to News")
        
class TopNews(models.Model):
    news=models.ForeignKey(Add_News,  on_delete=models.CASCADE)
    date=models.DateField( auto_now_add=False)
    news = AutoSlugField(populate_from='get_news_title', unique=True, null=True)

    def get_news_title(self):
        return self.news.title

    def __str__(self):
        return str(self.id)
    
class Populer(models.Model):
    news=models.ForeignKey(Add_News, on_delete=models.CASCADE)
    populer_slug=AutoSlugField(populate_from='get_news_title', unique=True, null=True)
    date=models.DateField( auto_now_add=True)
    
    
class News_populer(models.Model):
    news=models.ForeignKey(Add_News, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateTimeField( auto_now_add=True)
    populer_slug=AutoSlugField(populate_from='get_news_title',unique=True, null=True)
    
    def __str__(self):
        return self.news.title
    
class Super_news(models.Model):
    news=models.ForeignKey(Add_News, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    super_slug = AutoSlugField(populate_from='news_title', unique=True, null=True)
    
    def __str__(self):
     return self.news.title

    @property
    def news_title(self):
        return self.news.title
    
class top_news(models.Model):
    news=models.ForeignKey(Add_News, on_delete=models.CASCADE)
    date=models.DateField( auto_now_add=True)
    top_slug = AutoSlugField(populate_from='news_title', unique=True, null=True)
    
    def __str__(self):
        return self.news.title
    
    @property
    def news_title(self):
        return self.news.title
    