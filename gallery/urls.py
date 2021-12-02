from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',views.index,name='index'),
  path('search/',views.search_results,name='search_results'),
  path('images/<int:image_id>/',views.get_image_by_id, name ='get_image_by_id'),
  path('images/<location>/',views.filter_by_location,name= 'filter_by_location'),
  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)