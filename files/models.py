from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class FileUpload(models.Model):
    file_label = models.CharField(null=True, default=None, max_length=500)
    file_url = models.CharField(null=True, default=None, max_length=1000)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class DirectFileUpload(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name
