from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('detalle/<int:pk>', views.NoticiaDetailView.as_view()),
    
]