from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def gallery(request):
    category = request.GET.get('categories')
    if category == None:
        imagesCard = Photo.objects.all() 

    else:
        imagesCard = Photo.objects.filter(categorey__name=category) 
    categories = Categorey.objects.all()
    
    context={
        "categories" :categories,
        "imagesCard":imagesCard
    }
    return render(request, 'photos/gallery.html',context )

def addPhoto(request):
    categories = Categorey.objects.all()
    if request.method == "POST":
        data= request.POST
        image = request.FILES.get('image')

        if data['category'] != 'null':
            category = Categorey.objects.get(id=data['category'])
        elif data['newCategory'] != '':
            category,created = Categorey.objects.get_or_create(name =data['newCategory'])

        else:
            category =None

        photo = Photo.objects.create(
            categorey = category,
            description = data['description'],
            image = image
        )
        return redirect('gallery')
        
    context={
        "categories" :categories,
        
    }
    return render(request, 'photos/add.html',context )

def viewPhoto(request,pk):
     image = Photo.objects.get(id=pk) 

     context={
         "image":image 
     }

     return render(request, 'photos/photo.html',context )


def deletePhoto(request,pk):
     order = Photo.objects.get(id=pk)
     if request.method == "POST":
      order.delete()
      return redirect('/')

      
         

     context ={
        'item':order
    }
     
      

     return render(request, 'photos/delete.html',context )