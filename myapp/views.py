from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myapp.serializers import UserSerializer, GroupSerializer, ProviderSerializer, ServiceSerializer
from myapp.models import Provider, ServiceAreas


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProviderViewSet(viewsets.ModelViewSet):
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer


class ServiceAreasViewSet(viewsets.ModelViewSet):
    queryset = ServiceAreas.objects.all()
    serializer_class = ServiceSerializer