from django.core.signals import request_started
from django.shortcuts import render
from .models import Startup_register
from .serializer import StartupSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
''' This is viewpage is for mixins go to myview page for Concreate genric view class'''
# Create your views here.
class  Startuplist(GenericAPIView,ListModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def get(self,request):
        return self.list(request)
class Createstartup(GenericAPIView,CreateModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def post(self,request):
        return self.create(request)
class Updatestartup(GenericAPIView,UpdateModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def post(self, request, *args, **kwargs):
        return self.update(request,**kwargs)
class Deletestartup(GenericAPIView,DestroyModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,**kwargs)
class Retrivestartup(GenericAPIView,RetrieveModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,**kwargs)


'''
class  Startuplist(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
This will perform both listing and creating according to the class name we need to change the url path
'''

'''
class Updatestartup(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Startup_register.objects.all()
    serializer_class = StartupSerializer
    def post(self, request, *args, **kwargs):
        return self.update(request,**kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,**kwargs)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,**kwargs)
This will perform delete, update and retrive  according to the class name we need to change the url path
'''