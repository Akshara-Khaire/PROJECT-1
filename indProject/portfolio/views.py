from django.shortcuts import render
from django.http import HttpResponse  # Added missing import

# Create your views here.
def home(request):
    return render(request, 'home.html') 
