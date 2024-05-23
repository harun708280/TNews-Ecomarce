from django.shortcuts import render
from.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

# def categories_processor(request):
#     categories = Cetagory.objects.all().order_by('-id')
#     return {'categories': categories}