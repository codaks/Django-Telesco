from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.

def index(request):
    dst1 = Destinations()
    dst1.id = 1
    dst1.name = "Goa"
    dst1.img = "static/images/destination_1.jpg"
    dst1.desc = "A very beautiful place full of beaches"
    dst1.price = 43000

    dst2 = Destinations()
    dst2.id = 2
    dst2.name = "Dehradun"
    dst2.img = "static/images/destination_2.jpg"
    dst2.desc = "A Place wchich is calm and quite"
    dst2.price = 36000

    dst3 = Destinations()
    dst3.id = 3
    dst3.name = "Haridwar"
    dst3.img = "static/images/destination_3.jpg"
    dst3.desc = "Temples All Around and Laxman jhula to visit"
    dst3.price = 40000

    dst4 = Destinations()
    dst4.id = 4
    dst4.name = "Delhi"
    dst4.img = "static/images/destination_4.jpg"
    dst4.desc = "Too crowded Place"
    dst4.price = 20000

    dst5 = Destinations()
    dst5.id = 5
    dst5.name = "Andamman And Nicobar"
    dst5.img = "static/images/destination_5.jpg"
    dst5.desc = "Beauty in Forrests"
    dst5.price = 50000

    dst6 = Destinations()
    dst6.id = 6
    dst6.name = "Agra"
    dst6.img = "static/images/destination_6.jpg"
    dst6.desc = "Place of Loveones"
    dst6.price = 39000

    destation_lists = [dst1,dst2,dst3,dst4,dst5,dst6]
    return render(request,'travello/index.html', {'destinations':destation_lists})