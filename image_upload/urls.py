from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload_list, name='image_upload_list'),
]
