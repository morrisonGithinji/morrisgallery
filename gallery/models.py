from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



  
class Location(models.Model): 
  name = models.CharField(max_length=30)
  
  def save_location(self):
    self.save()
    
  def delete_location(self):
    self.delete()   
   
  def __str__(self):
        return self.name  
    
class Category(models.Model):
  name = models.CharField(max_length=10)  
  
  def save_category(self):
    self.save()
    
  def delete_category(self):
    self.delete()  
    
  def __str__(self):
        return self.name    
    
    
class  Image(models.Model):
  image = CloudinaryField('image')
  name= models.CharField(max_length =10)
  description= models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  
  def save_image(self):
    self.save()
    
  def delete_image(self):
    self.delete()  
      
  @classmethod
  def search_by_category(cls, search_term):
    image = cls.objects.filter(category__name__icontains=search_term)
    return image 
     
  @classmethod
  def get_all(cls):
    image = cls.objects.all()
    return image
  
  @classmethod
  def filter_by_location(cls,location):
    images = cls.objects.filter(location__name=location)
    return images
  
  