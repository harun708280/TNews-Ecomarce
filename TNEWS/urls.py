
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('accaount/',include('Accaount.urls')),
]
