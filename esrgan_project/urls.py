# esrgan_project/urls.py
from django.urls import path
from esrgan_app.views import upscale_image,home

urlpatterns = [
    path('', home, name='home'),
    path('upscale/', upscale_image, name='upscale_image'),
]
