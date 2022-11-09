from django.contrib import admin

from education.models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
        list_display = ('name',)

