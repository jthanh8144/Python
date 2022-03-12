from django.urls import path
from . import views

app_name = 'uploadModel'
urlpatterns = [
    path('', views.uploadWModel.as_view(), name='upload'),
]
