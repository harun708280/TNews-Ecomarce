from django.shortcuts import render
from.models import *
# Create your views here.


def index(request):
    sp=Sub_cetagory.objects.get(name='Politics')
    sb=Sub_cetagory.objects.get(name='Business')
    ss=Sub_cetagory.objects.get(name='Sports')
    Movies=Sub_cetagory.objects.get(name='Movies')
    Weather=Sub_cetagory.objects.get(name='Weather')
    # Animal=Sub_cetagory.objects.get(name='Animal')
    # Fashions=Sub_cetagory.objects.get(name='Fashions')
    # Health=Sub_cetagory.objects.get('Health')
    # Travels=Sub_cetagory.objects.get('Travels')
    # Technology=Sub_cetagory.objects.get('Technology')
    # Food=Sub_cetagory.objects.get('Food')
    # Music=Sub_cetagory.objects.get('Music')
    
    pl=Add_News.objects.filter(sub_cetagory=sp).order_by('id')[:1]
    bussniess=Add_News.objects.filter(sub_cetagory=sb).order_by('id')[:1]
    sport=Add_News.objects.filter(sub_cetagory=ss).order_by('-id')[:1]
    all=Add_News.objects.all()[3:]
    top=top_news.objects.all().order_by('-id')[:4]
    rectent_news=Add_News.objects.all().order_by('-id')[:4]
    populer=Super_news.objects.all().order_by('-id')[:6]
    
    
    
    
    
    return render(request, 'index.html', {'politics_news':pl,'B':bussniess,'s':sport,'all':all,'t':top,'r':rectent_news,'p':populer})

def politics(request):
    sp=Sub_cetagory.objects.get(name='Politics')
    pl=Add_News.objects.filter(sub_cetagory=sp)
    return render(request,'cetagory/politics.html',locals())

def Business(request):
  sb=Sub_cetagory.objects.get(name='Business')
  buissnes=Add_News.objects.filter(sub_cetagory=sb) 
  return render(request,'cetagory/buisness.html',locals())

def Sports(request):
    ps=Sub_cetagory.objects.get(name='Sports')
    sports=Add_News.objects.filter(sub_cetagory=ps)
    return render(request,'cetagory/sports.html',locals())

def News_Details(request, slug):
    news = Add_News.objects.get(news_slug=slug)
    
    try:
        populer = Super_news.objects.get(super_slug=slug)
    except Super_news.DoesNotExist:
        populer = None
    
    try:
        top=top_news.objects.get(top_slug=slug)
    except top_news.DoesNotExist:
        
        top=None
    related_news = Add_News.objects.filter(sub_cetagory=news.sub_cetagory)
    recent = Add_News.objects.all().order_by('-id')[:4]
    
    return render(request, 'blog-details.html', {
        'news': news,
        'populer': populer,
        'related_news': related_news,
        'recent': recent,
        'top':top
    })

# def categories_processor(request):
#     categories = Cetagory.objects.all().order_by('-id')
#     return {'categories': categories}