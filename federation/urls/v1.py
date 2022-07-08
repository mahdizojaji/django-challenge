from django.urls import path

from ..views import CreateStadiumAPIView, CreateMatchAPIView, BuyMatchSeatPlaceAPIView

urlpatterns = [
    path("stadium/", CreateStadiumAPIView.as_view(), name="create_stadium_v1"),
    path("match/", CreateMatchAPIView.as_view(), name="create_match_v1"),
    path("match/<int:pk>/buy/", BuyMatchSeatPlaceAPIView.as_view(), name="buy_match_seat_place_v1"),
]
