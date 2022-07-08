from django.contrib import admin

from ..models import MatchSeatPlace


@admin.register(MatchSeatPlace)
class MatchSeatPlaceAdmin(admin.ModelAdmin):
    pass
