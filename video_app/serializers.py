from rest_framework import serializers
from video_app.models import Videos


class VideosListSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"
