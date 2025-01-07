from rest_framework import serializers
from .models import *
class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Startup_register
        fields='__all__'