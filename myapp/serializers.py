from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from myapp import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Provider
		fields = ('name', 'email', 'phone_number', 'language', 'currency')


class ServiceSerializer(GeoFeatureModelSerializer):
	
	class Meta:
		model = models.ServiceAreas
		geo_field = "geo_json"
		fields = ('provider', 'geo_json')