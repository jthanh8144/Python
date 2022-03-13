from django.urls import path
from . import views

app_name = 'umf'
urlpatterns = [
    path('', views.uploadMultiFile.as_view(), name='upload'),
    # path('', views.list)
]
