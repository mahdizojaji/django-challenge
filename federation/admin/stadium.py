from django.contrib import admin

from ..models import Stadium


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    pass
