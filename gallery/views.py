
from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def index(request):
  images= Image.get_all()
  location= Location.objects.all()
  return render(request, 'index.html',{'images':images, "location":location})


def search_results(request):
  
  if 'image' in request.GET and request.GET["image"]:
    search_term = request.GET.get("image")
    searched_images = Image.search_by_category(search_term)
    message = f"{search_term}"
    
    return render(request,"search.html", {'message':message,'images':searched_images})
  else:
    message = "Please input a valid term"
    return render(request,'search.html', {'message':message})
  
def get_image_by_id(request,image_id):
  try:
    image= Image.objects.get(id=image_id)
  except DoesNotExist:
    raise Http404()  
  return render(request,'display.html',{'image':image})

def filter_by_location(request,location):
  image= Image.filter_by_location(location)
  
  
  return render(request,'location.html',{'images':image})
  