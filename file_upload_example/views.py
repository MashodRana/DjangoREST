from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializers


# Create your views here.
class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_srz = FileSerializers(data=request.data)
        # print(request.data)
        if file_srz.is_valid():
            file_srz.save()
            return Response(file_srz.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_srz.errors, status=status.HTTP_400_BAD_REQUEST)
