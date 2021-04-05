from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('showall/', views.showall, name='showall'),
    path('result/', views.result, name='result'),
]
