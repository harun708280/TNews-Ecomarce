from django.urls import path

from.import views,context_processors
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('news_detail/<slug>',views.News_Details,name='details'),
    
    # path('d',context_processors.Cetagory_url)
    path('politcs/',views.politics,name='politics'),
    path('buissnes/',views.Business,name='buissnes'),
    path('sports/',views.Sports,name='sport')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
