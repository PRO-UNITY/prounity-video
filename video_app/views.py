from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from video_app.models import Videos
from video_app.serializers import VideosListSerialiers


class VideosViews(APIView):
    def get(self, request, pk, format=None):
        instance = Videos.objects.get(id=pk)
        serializers = VideosListSerialiers(instance)
        return Response(serializers.data, status=status.HTTP_200_OK)
