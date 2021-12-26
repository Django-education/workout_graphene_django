from django.contrib import admin
from .models import Workout, Tag


@admin.register(Workout)
class PostAdmin(admin.ModelAdmin):
    model = Workout

    list_display = (
        "id",
        "title",
        "description",
        "place",
        "date",
    )
    list_filter = (
        "date",
    )
