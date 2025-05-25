from django.shortcuts import render
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from oners.models import Rentales

# Create your views here.


def home(request):
    home_rentals = []
    for i in Rentales.objects.all():
        home_rentals.append(i)
        if len(home_rentals) == 3:
            break
    return render(request, 'index.html', {"home_rentals": home_rentals})
