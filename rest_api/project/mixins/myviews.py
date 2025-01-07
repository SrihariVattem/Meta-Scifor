from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Startup_register
from .serializer import StartupSerializer

class Listview(ListAPIView):
    queryset =Startup_register.objects.all()
    serializer_class = StartupSerializer
class Creatview(CreateAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class Retrieveview(RetrieveAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class Destroyview(DestroyAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class Updateview(UpdateAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class lsview(ListCreateAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class ruview(RetrieveUpdateAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class rdview(RetrieveDestroyAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
class rudview(RetrieveUpdateDestroyAPIView):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer





