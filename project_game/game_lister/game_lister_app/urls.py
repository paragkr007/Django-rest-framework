# -*- coding: utf-8 -*-
from django.urls import path
from game_lister_app import views

urlpatterns = [
    path('app_name/',views.Gamer_api.display_text,name='display'),
    path('search/',views.Gamer_api.search_data,name='search_data')
]

