from django.urls import path
from posts import views 
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [

    path('Upload/', views.upload_profile, name='Upload')
]






if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 