from django .urls import path
from.forms import *
from.import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('accaount/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginFrom),name='login'),
    path('accaount/logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('accaount/registration/',views.Registration,name='registration'),
]
