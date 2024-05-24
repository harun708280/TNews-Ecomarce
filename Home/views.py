from django.shortcuts import render
from.models import *
# Create your views here.


def index(request):
    sp=Sub_cetagory.objects.get(name='Politics')
    sb=Sub_cetagory.objects.get(name='Business')
    ss=Sub_cetagory.objects.get(name='Sports')
    pl=Add_News.objects.filter(sub_cetagory=sp).order_by('id')[:1]
    bussniess=Add_News.objects.filter(sub_cetagory=sb).order_by('id')[:1]
    sport=Add_News.objects.filter(sub_cetagory=ss)
    all=Add_News.objects.all()[3:]
    top_news=Add_News.objects.all()[4:8]
    rectent_news=Add_News.objects.all().order_by('-id')[:4]
    return render(request, 'index.html', {'politics_news':pl,'B':bussniess,'s':sport,'all':all,'t':top_news,'r':rectent_news})


def News_Details(request,pk):
    news=Add_News.objects.get(pk=pk)
    related_news=Add_News.objects.filter(sub_cetagory=news.sub_cetagory)
    recent=Add_News.objects.all().order_by('-id')[:4]
    return render(request,'blog-details.html',locals())
# def categories_processor(request):
#     categories = Cetagory.objects.all().order_by('-id')
#     return {'categories': categories}