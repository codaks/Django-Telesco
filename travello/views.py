from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.

def index(request):
    destinations = Destinations.objects.all()


    return render(request,'travello/index.html', {'destinations':destinations})