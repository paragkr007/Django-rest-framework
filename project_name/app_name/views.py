from django.shortcuts import render
from django.urls import path,include
from django.http import HttpResponse

def display_text(request):
    return HttpResponse("<h3>This is my world!</h3>")
