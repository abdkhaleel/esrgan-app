# views.py
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import cv2
from cv2 import dnn_superres
import base64
import torch
from RealESRGAN import RealESRGAN
from PIL import Image
import numpy as np

def upscale_image(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle uploaded image
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        image_path = fs.save(uploaded_image.name, uploaded_image)

        # Super-resolution upscaling
        # super_res = dnn_superres.DnnSuperResImpl_create()

        # # Path to the pre-trained model
        # model_path = 'EDSR_x4.pb'  # Adjust MODEL_ROOT to your model directory

        # # Load the pre-trained model
        # super_res.readModel(model_path)
        # super_res.setModel('edsr', 4)

        # super_res.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        # super_res.setPreferableTarget(cv2.dnn.DNN_BACKEND_CUDA)

        # Read the uploaded image
        img = Image.open(settings.MEDIA_ROOT + '/' + image_path).convert('RGB') # Adjust MEDIA_ROOT to your media directory
        img_np = np.array(img)

        # Upscale the image
        # upscaled = super_res.upsample(img)

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        model = RealESRGAN(device, scale=8)
        model.load_weights('weights/RealESRGAN_x8.pth', download=True)

        upscaled = model.predict(img_np)
        upscaled_np = np.array(upscaled)

        # Convert original and upscaled images to base64
        _, encoded_original_img = cv2.imencode('.jpg', cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))
        _, encoded_upscaled_img = cv2.imencode('.jpg', cv2.cvtColor(upscaled_np, cv2.COLOR_RGB2BGR))
        original_img = base64.b64encode(encoded_original_img).decode('utf-8')
        upscaled_img = base64.b64encode(encoded_upscaled_img).decode('utf-8')

        # Rendering the images in HTML template
        context = {
            'original_img': original_img,
            'upscaled_img': upscaled_img,
        }
        return render(request, 'upscaled_image.html', context)

    return render(request, 'upload_image.html')
