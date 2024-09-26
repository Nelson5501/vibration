# myapp/urls.py
from django.conf import settings # type: ignore
from django.contrib import admin # type: ignore
from .views import player, home, podcast, emissions, charts, teams, news, contact, newevents
from django.urls import path, include # type: ignore
from . import views
from django.urls import path

urlpatterns = [
    path('',home, name='home'),
    path('player', player, name='radio player'),
    path('podcast', podcast, name='podcast'),
    path('emissions', emissions, name='emission'),
    path('charts', charts, name='charts'),
    path('teams', teams, name='teams'),
    path('news', news, name='news'),
    path('newevents', newevents, name='newevents'),
    path('contact', contact, name='contact'),
 
]

    
