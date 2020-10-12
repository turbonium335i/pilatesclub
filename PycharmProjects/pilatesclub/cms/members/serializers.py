from rest_framework import serializers
from .models import client

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = '__all__'