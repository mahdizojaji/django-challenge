from django.contrib import admin

from ..models import StadiumSeatPlace


@admin.register(StadiumSeatPlace)
class StadiumSeatPlaceAdmin(admin.ModelAdmin):
    pass
