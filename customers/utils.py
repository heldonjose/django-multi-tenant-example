from django.db import connections
from django_tenants.utils import get_tenant_database_alias


def get_current_schema():
    tenant = connections[get_tenant_database_alias()]
    return tenant.schema_name
