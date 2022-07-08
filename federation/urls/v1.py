from django.urls import path

from ..views import CreateStadiumAPIView, CreateMatchAPIView

urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium_v1"),
    path("match/", CreateMatchAPIView.as_view(), name="create_match_v1"),
]
