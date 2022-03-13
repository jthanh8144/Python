from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.registerUser.as_view(), name='register'),
    path('login/', views.loginUser.as_view(), name='login'),
    path('private/', views.privateUser.as_view(), name='private'),
    path('logout/', views.logoutUser, name='logout'),
]
