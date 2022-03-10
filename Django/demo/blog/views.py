from django.http import HttpResponse
from django.shortcuts import render
from .models import postForm


def index(request):
    pF = postForm.objects.all()
    return render(request, 'blog/index.html', {'pF': pF})

def postDetail(request, id):
    pD = postForm.objects.get(id = id)
    return render(request, 'blog/postDetail.html', {'pD': pD})