# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django_tenants.management.commands import BaseTenantCommand
from django_tenants.utils import schema_context

from cms.models import Category
from customers.models import Client, Domain


# manage.py tenant_command do_foo --schema=tenant1
class Command(BaseCommand):
# class Command(BaseTenantCommand):
    help = 'Update performance cycles status'

    def handle(self, **options):
        print(Category.objects.all())
        # with schema_context('tenant1'):
        #     print('asdasd')
        #     print(Category.objects.all())

