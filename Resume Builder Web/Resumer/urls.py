from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inform/<key>', views.inform, name='inform'),
    path('search', views.search, name='search'),
    path('eduform', views.eduform, name='eduform'),
    path('orgform', views.orgform, name='orgform'),
    path('expform', views.expform, name='expform'),
    # path('eduform', views.eduform, name='eduform'),
    # path('orgform', views.orgform, name='orgform'),
    # path('expform', views.expform, name='expform'),
    path('resume', views.resume, name='resume'),
]
