from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Gamer
# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.permissions import IsAuthenticated

class Gamer_api(APIView):
  permission_classes = (IsAuthenticated,)
  
  def display_text(request):
      allgames = Gamer.objects.all()
      print(allgames)
      #return JsonResponse({'games':'hello'})
      return render(request, 'base.html' ,{'data':allgames})
  
  
  def search_data(request):
      title= request.GET['title']
      print(title)
      allgames = Gamer.objects.all().filter(title=title)
      print(allgames)
      #return JsonResponse({'games':'hello'})
      return render(request, 'base.html' ,{'data':allgames})  