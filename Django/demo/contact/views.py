from django.http import HttpResponse
from django.shortcuts import render
from .forms import contact_Form

def index(request):
    # cf = contact_Form
    context = {'cf': contact_Form}
    return render(request, 'contact/index.html', context)

def getContact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse('save successful')
    else:
        return HttpResponse('not POST')
