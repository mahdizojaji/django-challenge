from django.urls import path

from ..views import SendCodeAPIView

urlpatterns = [
    path("send_code/", SendCodeAPIView.as_view(), name="send_code_v1"),
]
