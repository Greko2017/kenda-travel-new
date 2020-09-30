from django.urls import path, include
from . import views


from django.urls import path
from .api import LocationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('location', LocationViewSet, 'location')

urlpatterns = router.urls
urlpatterns += path('auth/', include('account.urls')),