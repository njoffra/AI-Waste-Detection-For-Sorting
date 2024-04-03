from rest_framework import generics, status
from rest_framework.response import Response
from .models import RecognitionResult
from .serializers import RecognitionResultSerializer


class RecognitionResultListCreate(generics.ListCreateAPIView):
    queryset = RecognitionResult.objects.all()
    serializer_class = RecognitionResultSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)