from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer

from rest_framework import viewsets, permissions

from travellite.models import Location
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/location-list/',
		'Detail View':'/location-detail/<str:pk>/',
		'Create':'/location-create/',
		'Update':'/location-update/<str:pk>/',
		'Delete':'/location-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def locationList(request):
	locations = Location.objects.all()
	serializer = LocationSerializer(locations, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def locationDetail(request, pk):
	locations = Location.objects.get(id=pk)
	serializer = LocationSerializer(locations, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def locationCreate(request):
	serializer = LocationSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def locationUpdate(request, pk):
	location = Location.objects.get(id=pk)
	serializer = LocationSerializer(instance=location, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def locationDelete(request, pk):
	location = Location.objects.get(id=pk)
	location.delete()

	return Response('Item succsesfully delete!')



