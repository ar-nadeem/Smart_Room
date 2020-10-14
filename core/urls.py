from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.main, name='main'),
    path('relay1', views.relay1, name='relay1'),
    path('relay2', views.relay2, name='relay2'),
    path('relay3', views.relay3, name='relay3'),
    path('relay4', views.relay4, name='relay4'),
    path('relay5', views.relay5, name='relay5'),
    path('relay6', views.relay6, name='relay6'),
    path('relay7', views.relay7, name='relay7'),
    path('relay8', views.relay8, name='relay8'),    
    
    path('all_on', views.all_on, name='all_on'),
    path('all_off', views.all_off, name='all_off'),
    




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)