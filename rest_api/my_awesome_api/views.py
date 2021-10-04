from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from my_awesome_api.serializers import PersonSerializer, SpeciesSerializer
from my_awesome_api.models import Person, Species


class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer