# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django_tenants.utils import schema_context

from cms.models import Category
from customers.models import Client, Domain


def create_schemas():
    tenant = Client(schema_name='public',
                    name='Schemas Inc.',
                    paid_until='2016-12-05',
                    on_trial=False)
    tenant.save()

    # Add one or more domains for the tenant
    domain = Domain()
    domain.domain = '127.0.0.1'  # don't add your port or www here! on a local server you'll want to use localhost here
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

    tenant = Client(schema_name='tenant1',
                    name='HELDON JOSE',
                    paid_until='2014-12-05',
                    on_trial=True)
    tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!

    # Add one or more domains for the tenant
    domain = Domain()
    domain.domain = 'localhost'  # don't add your port or www here!
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()



class Command(BaseCommand):
    help = 'Update performance cycles status'

    def handle(self, **options):
        Category.objects.all().delete()

        with schema_context('tenant1'):
            Category.objects.all().delete()

