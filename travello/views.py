from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destinations
# Create your views here.

def index(request):
    destinations = Destinations.objects.all()

    if request.session.has_key('username'):
        return render(request,'travello/index.html', {'destinations':destinations})
    else:
        return redirect('/accounts/login')
