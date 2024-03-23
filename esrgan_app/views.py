# views.py
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import cv2
from cv2 import dnn_superres
import base64

def upscale_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle uploaded image
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        image_path = fs.save(uploaded_image.name, uploaded_image)

        # Super-resolution upscaling
        super_res = dnn_superres.DnnSuperResImpl_create()

        # Path to the pre-trained model
        model_path = 'LapSRN_x8.pb'  # Adjust MODEL_ROOT to your model directory

        # Load the pre-trained model
        super_res.readModel(model_path)
        super_res.setModel('lapsrn', 8)

        # Read the uploaded image
        img = cv2.imread(settings.MEDIA_ROOT + '/' + image_path)  # Adjust MEDIA_ROOT to your media directory

        # Upscale the image
        upscaled = super_res.upsample(img)

        # Convert original and upscaled images to base64
        _, encoded_original_img = cv2.imencode('.jpg', img)
        _, encoded_upscaled_img = cv2.imencode('.jpg', upscaled)
        original_img = base64.b64encode(encoded_original_img).decode('utf-8')
        upscaled_img = base64.b64encode(encoded_upscaled_img).decode('utf-8')

        # Rendering the images in HTML template
        context = {
            'original_img': original_img,
            'upscaled_img': upscaled_img,
        }
        return render(request, 'upscaled_image.html', context)

    return render(request, 'upload_image.html')
