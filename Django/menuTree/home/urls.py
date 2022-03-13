from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # path('', views.uploadWModel.as_view(), name='upload'),
    path('', views.index)
]
