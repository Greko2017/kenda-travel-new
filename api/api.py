from travellite.models import Location
from rest_framework import viewsets, permissions
from api.serializers import LocationSerializer

# Location Viewset


class LocationViewSet(viewsets.ModelViewSet):
	queryset = Location.objects.all()

	serializer_class = LocationSerializer

	permission_classes = [
		permissions.IsAuthenticated
	]
	def get_queryset(self):
		return Location.objects.all()

	# def perform_create(self, serializer):
	# 	serializer.save(owner=self.request.user)