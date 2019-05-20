from django.urls import path
from app_name import views

urlpatterns = [
    path('app_name/',views.display_text,name='display')
]


'''
Deprecated : 

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
        path('project_app/<int:pk>/', views.project_app_detail), #<int:pk> -- when u have to pass an int as argument)
        

'''