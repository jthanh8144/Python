from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import uploadMulti
from . models import formUpload
from django.views.generic.edit import FormView

class uploadMultiFile(FormView):
    def get(self, request):
        form = uploadMulti
        return render(request, 'uploadMultiFile/index.html', { "form": form})

    def post(self, request):
        form = self.get_form(uploadMulti)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for file in files:
                instance = formUpload(image=file)
                instance.save()
            return HttpResponse('save success')