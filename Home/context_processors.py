from .models import *

def categories_processor(request):
    categories = Cetagory.objects.all()
    return {'categories': categories}

def Subcetagoris(request):
    sub_cetagory=Sub_cetagory.objects.all()
    return{'sub_cetagory':sub_cetagory}

def NavImages(request):
    image=NavImage.objects.all()
    return{'image':image}