from django.urls import path

from ..views import CreateStadiumAPIView

urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium_v1"),
]
