
from django.urls import path


from files.views import *

urlpatterns = [
    path("file_upload/", FileUploadView.as_view(), name="file_upload"),
    path('file_upload/<int:id>/', FileUploadSingleView.as_view(), name="file_upload_single"),
]
