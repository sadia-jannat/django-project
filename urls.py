from django.contrib import admin

from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='food-home'),
    path('about/',views.about,name='food-about'),
    path('bmi/',views.bmi,name='bmi'),
    path('chart/',views.chart,name='chart'),
    path('other/',views.other,name='other'),
    path('add/',views.add,name='add'),
    path('res/',views.res,name='res'),

    path('cal', views.cal, name='calculation'),

    path('math/',views.math,name='math'),

    path('teatment/', views.teatment, name='teatment'),

    path('brain/', views.brain, name='brain'),

    path('health/', views.health, name='health'),

    path('food/',views.food,name='food'),

    path('women/', views.women, name='women'),

    #pactis 2

    path('welcome/', views.welcome, name='welcome'),









]