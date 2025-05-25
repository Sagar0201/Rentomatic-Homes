from django.shortcuts import render
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from oners.models import Rentales

# Create your views here.


def home(request):
    try:
        home_rentals = list(Rentales.objects.all()[:3])
    except Rentales.DoesNotExist:
        home_rentals = []

    return render(request, 'index.html', {"home_rentals": home_rentals})
