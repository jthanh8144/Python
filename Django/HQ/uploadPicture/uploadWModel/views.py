from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . forms import UploadFileForm
from . models import UpForm

class uploadWModel(View):
    def get(self, request):
        uf = UploadFileForm
        return render(request, 'uploadWModel/index.html', {'uf': uf})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Save file success')
        return HttpResponse('Save file fail')

        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     instance = UpForm(image=request.FILES['image'])
        #     instance.save()
        #     return HttpResponse('Save file success')
        # return HttpResponse('Save file fail')
