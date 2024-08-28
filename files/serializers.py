# serializers.py

from rest_framework import serializers
from files.models import FileUpload, DirectFileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'


class DirectFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectFileUpload
        fields = ['name', 'file']
