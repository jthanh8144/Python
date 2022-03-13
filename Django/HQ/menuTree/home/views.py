from django.shortcuts import render
from . models import catagory

def index(request):
    listCatagory = catagory.objects.all()
    return render(request, 'home/index.html', { "listCatagory": listCatagory })
