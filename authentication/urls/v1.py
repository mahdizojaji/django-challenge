from django.urls import path

from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

from ..views import SendCodeAPIView, LoginAPIView

urlpatterns = [
    path("send_code/", SendCodeAPIView.as_view(), name="send_code_v1"),
    path("login/", LoginAPIView.as_view(), name="login_v1"),
    path("refresh/", get_refresh_view().as_view(), name="token_refresh_v1"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify_v1"),
]
