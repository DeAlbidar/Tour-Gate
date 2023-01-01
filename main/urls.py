from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About Us'),
    path('contact/', views.contact, name='Contact Us'),
    path('gallery/', views.gallery, name='Gallery'),
    path('create/', views.create, name='Create'),
    path('drive/', views.drive, name='Drive'),
    path('faq/', views.faq, name='FAQ'),
    path('view/', views.view, name='view'),
    path('view/<int:id>', views.view_details, name='view'),
    path('folder/<int:id>', views.folder_details, name='folder_details'),
    path('folder/', views.folder, name='folder'),
    path('upload_file/<int:id>', views.upload_file, name='Upload File'),
]