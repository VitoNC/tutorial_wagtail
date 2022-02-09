from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from rest_framework import permissions

from .models import Pelicula
from .serializers import PeliculaSerializer

'''
GenericViewSet  # generic view functionality
CreateModelMixin  # handles POSTs
RetrieveModelMixin  # handles GETs for 1 object
UpdateModelMixin,  # handles PUTs and PATCHes
ListModelMixin):  # handles GETs for many objects
'''


class PeliculaViewSet(ListModelMixin, GenericViewSet):  # handles GETs for many Companies
    ''' 
    API Endpoint para mostrar películas
    '''

    serializer_class = PeliculaSerializer
    queryset = Pelicula.objects.all().order_by('-rating')
    # permission_classes = [permissions.IsAuthenticated]
