from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from cms.models import Category
from customers.utils import get_current_schema


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    # def has_delete_permission(self, request, obj=None):
    #     if get_current_schema() != 'public':
    #         return False
    #     return True
