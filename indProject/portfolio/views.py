from django.shortcuts import render
from django.http import HttpResponse  # Added missing import

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def portfolio(request):
    return render(request,'portfolio.html') 