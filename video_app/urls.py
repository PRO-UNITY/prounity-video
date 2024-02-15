from django.urls import path
from video_app.views import VideosViews

urlpatterns = [
    path('<int:pk>', VideosViews.as_view())
]