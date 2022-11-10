from django.db import models, connections
from django.db.models import QuerySet
from django_tenants.utils import get_tenant_base_schema, get_tenant_database_alias
from django.core.exceptions import ValidationError


class SoftDeleteModelQuerySet(QuerySet):

    def delete(self):
        print('connections', connections)
        print('connections', get_tenant_database_alias)
        tenant = connections[get_tenant_database_alias()]
        print('t', tenant.schema_name)
        if tenant.schema_name != 'public':
            raise ValidationError('Somente o admin pode deletar essa categoria')
        [x.delete() for x in self]


class CategoryManager(models.Manager):


    def get_queryset(self):
        print('get_queryset')
        return SoftDeleteModelQuerySet(self.model)


# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
    objects = CategoryManager()


