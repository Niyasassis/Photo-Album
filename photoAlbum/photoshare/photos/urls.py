from django.urls import path,include
from . import views

urlpatterns = [
   
    path('', views.gallery, name="gallery"),
    path('add', views.addPhoto,name="add"),
    path('view/<str:pk>/', views.viewPhoto,name="view"),
    path('delete/<str:pk>/', views.deletePhoto, name="delete"),
]