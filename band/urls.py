from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    #path ('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('band/', views.band, name='band'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]