from django.shortcuts import render
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from oners.models import Rentales

# Create your views here.


def home(request):
    try:
        home_rentals = list(Rentales.objects.all()[:3])
        if not home_rentals:
            # If no data found, handle accordingly (e.g., empty list or custom message)
            home_rentals = []
    except Exception as e:
        # Log the exception if needed
        print(f"Error fetching rentals: {e}")
        home_rentals = []  # fallback to empty list

    return render(request, 'index.html', {"home_rentals": home_rentals})

