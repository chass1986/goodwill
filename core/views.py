from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Territories
from .serializers import TerritoriesSerializer


class IndexApiView(APIView):
    def get(self, request):
        return Response('Welcome !!!', status=status.HTTP_200_OK)


class CountriesApiView(APIView):
    def get(self, request):
        countries = Territories.objects.filter(kind='FRPAYS').order_by('name')
        serializer = TerritoriesSerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionsApiView(APIView):
    def get(self, request, country_id=1):
        regions = Territories.objects.filter(parent_id=country_id, kind='FRREGI').order_by('name')
        serializer = TerritoriesSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DepartmentApiView(APIView):
    def get(self, request, region_id):
        deps = Territories.objects.filter(parent_id=region_id, kind='FRDEPA')
        serializer = TerritoriesSerializer(deps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


