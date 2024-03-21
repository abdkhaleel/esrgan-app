from django.shortcuts import render

# Create your views here.
# esrgan_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from .utils import esrgan_upscale

def upscale_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = request.FILES['image']
            upscaled_image = esrgan_upscale(uploaded_image)
            return render(request, 'upscaled_image.html', {'upscaled_image': upscaled_image})
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})
