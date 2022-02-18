from django.conf.urls.static import static
from django.urls import path, include, re_path
from restaurant import settings
from django.views.static import serve
from core import views

urlpatterns = [
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)