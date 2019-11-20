from django.shortcuts import render

from django.views.generic import ListView,DetailView
from .page import StandardResultsSetPagination
from rest_framework import viewsets
from .models import Asset,IDC,Cabinet,Server,Memory,Disk,SysUsers
from .serializers import (AssetSerializer,IDCSerializer,ServerSerializer,
                                    SysUsersSerializer,MemorySerializer,
                                    DiskSerializer,CabinetSerializer)
# Create your views here.


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    pagination_class = StandardResultsSetPagination


class IDCViewSet(viewsets.ModelViewSet):
    queryset = IDC.objects.all()
    serializer_class = IDCSerializer
    pagination_class = StandardResultsSetPagination


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    pagination_class = StandardResultsSetPagination


class SysUsersViewSet(viewsets.ModelViewSet):
    queryset = SysUsers.objects.all()
    serializer_class = SysUsersSerializer
    pagination_class = StandardResultsSetPagination


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    pagination_class = StandardResultsSetPagination
 

class MemoryViewSet(viewsets.ModelViewSet):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer
    pagination_class = StandardResultsSetPagination


class DiskViewSet(viewsets.ModelViewSet):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    pagination_class = StandardResultsSetPagination


class AssetDetail(DetailView):
    model = Asset
    context_object_name = "asset"
    template_name = "detail.html"

