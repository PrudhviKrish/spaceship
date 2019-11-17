from django.shortcuts import render
from .models import img
# Create your views here.

def index(request):
    image1  = img()
    image1.name = "Krish"
    image1.image = "project-image1.jpg"
    return render(request, 'index.html', {'image1': image1})