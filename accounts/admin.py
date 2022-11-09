from django.contrib import admin

# Register your models here.
from accounts.models import User


@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
        list_display = ('name', 'created_at')