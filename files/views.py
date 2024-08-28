from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from files.models import FileUpload, DirectFileUpload
from files.serializers import FileUploadSerializer, DirectFileUploadSerializer
from files.utils.upload_to_s3_utils import UploadToS3


class FileUploadView(ListCreateAPIView):
    serializer_class = FileUploadSerializer
    pagination_class = PageNumberPagination
    permission_classes = IsAuthenticated,
    queryset = FileUpload.objects.all()

    def post(self, request, *args, **kwargs):
        for label, file in request.FILES.items():
            try:
                status, file_upload, message = UploadToS3.upload_file(
                    label=label,
                    user_id=request.user and request.user.pk,
                    file_object=file.file,
                    name=file.name
                )
                if status and file_upload:
                    return Response({"status": "success", "data": FileUploadSerializer(file_upload).data})
                return Response({"status": "error", "message": message}, status=HTTPStatus.BAD_REQUEST)
            except Exception as e:
                raise e
        return Response()


class FileUploadSingleView(RetrieveUpdateDestroyAPIView):
    serializer_class = FileUploadSerializer
    pagination_class = PageNumberPagination
    permission_classes = IsAuthenticated,
    queryset = FileUpload.objects.all()
    lookup_field = "id"


class DirectFileUploadViewSet(viewsets.ModelViewSet):
    queryset = DirectFileUpload.objects.all()
    serializer_class = DirectFileUploadSerializer
