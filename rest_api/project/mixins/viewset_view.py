from django.shortcuts import render
from .models import Startup_register
from .serializer import StartupSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class Startupviews(viewsets.ViewSet):
    def list(self,request):
        queryset= Startup_register.objects.all()
        serializer=StartupSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset = Startup_register.objects.get(id=id)
            serializer = StartupSerializer(queryset)
            return Response(serializer.data)
    def update(self,request,pk):
        id=pk
        queryset= Startup_register.objects.get()
        serializer=StartupSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Successfully updated'})

    def destroy(self,request,pk):
        id=pk
        queryset= Startup_register.objects.get(pk=id)
        queryset.delete()
        return Response({'msg: deleted'})

    def create(self,request):
        serializer=StartupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: successfully created'})
