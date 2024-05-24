from django.shortcuts import render
from.models import *
# Create your views here.


def index(request):
    sb=Sub_cetagory.objects.get(name='Politics')
    pl=Add_News.objects.filter(sub_cetagory=sb).order_by('id')[:1]
    
    return render(request, 'index.html', {'politics_news':pl})
# def categories_processor(request):
#     categories = Cetagory.objects.all().order_by('-id')
#     return {'categories': categories}