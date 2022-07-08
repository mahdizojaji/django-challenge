from django.urls import path

from ..views import SendCodeAPIView, LoginAPIView

urlpatterns = [
    path("send_code/", SendCodeAPIView.as_view(), name="send_code_v1"),
    path("login/", LoginAPIView.as_view(), name="login_v1"),
]
