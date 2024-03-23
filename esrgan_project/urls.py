from django.contrib import admin
from django.urls import path
from esrgan_app.views import upscale_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upscale_image, name='home'),  # Add this line to define the root URL pattern
    path('upscale/', upscale_image, name='upscale_image'),
]
