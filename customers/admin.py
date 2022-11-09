from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from customers.models import Client, Domain


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until', 'schema_name')

@admin.register(Domain)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('domain', 'tenant', 'is_primary')
