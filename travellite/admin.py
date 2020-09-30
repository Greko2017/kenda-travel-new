from django.contrib import admin
from .models import User, Location, Flight

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ['city', 'region']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
	list_display = ['companyName', 'sourceLocation','destinationLocation']