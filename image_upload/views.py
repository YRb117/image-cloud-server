from django.shortcuts import render, redirect
# Create your views here. 
from .forms import ImageUploadForm
from .models import UploadedImage
import os 
import boto3
from image_upload_service import settings

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # image = form.cleaned_data['image']
            # # instance = UploadedImage(image=image)
            # # instance.save()
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = UploadedImage.objects.all()
    existing_images = [img for img in images if os.path.exists(os.path.join(settings.MEDIA_ROOT, img.image.name))]
    print(len(existing_images))
    return render(request, 'image_list.html', {'images': images})

def image_upload_list(request):
    images = UploadedImage.objects.all()
    existing_images = [img for img in images if os.path.exists(os.path.join(settings.MEDIA_ROOT, img.image.name))]
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_upload_list')
    else:
        form = ImageUploadForm()

    return render(request, 'image_upload_list.html', {'form': form, 'images': images})