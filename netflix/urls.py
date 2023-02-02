from django.urls import path 
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main,name='main'),
    path('movie',views.movie,name='movie')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)