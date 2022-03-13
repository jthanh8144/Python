from django.http import HttpResponse
from django.shortcuts import render
from .forms import contact_Form
from .models import contactForm
from django.views import View

class contact(View):
    def get(self, request):
        cf = contact_Form
        return render(request, 'contact/index.html', {'cf': cf})

    def post(self, request):
        if request.method == "POST":
            cf = contact_Form(request.POST)
            if cf.is_valid():
                saveCF = contactForm(username=cf.cleaned_data['username'],
                                    email=cf.cleaned_data['email'],
                                    body=cf.cleaned_data['body'])
                saveCF.save()
                return HttpResponse('save success')
        else:
            return HttpResponse('not post')
