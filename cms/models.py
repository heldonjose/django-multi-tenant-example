from itertools import chain

from django.db import models, connections
from django.db.models import QuerySet
from django_tenants.utils import get_tenant_base_schema, get_tenant_database_alias, schema_context
from django.core.exceptions import ValidationError

from customers.utils import get_current_schema


class SoftDeleteModelQuerySet(QuerySet):

    def delete(self):
        print('connections', connections)
        print('connections', get_tenant_database_alias)
        schema_name = get_current_schema()
        print('t', schema_name)
        if schema_name != 'public':
            raise ValidationError('Somente o admin pode deletar essa categoria')
        [x.delete() for x in self]


class CategoryManager(models.Manager):

    def get_queryset(self):
        qs = SoftDeleteModelQuerySet(self.model)
        # print('qs', qs)
        qs_public = None
        # with schema_context('public'):
        #     qs_public = SoftDeleteModelQuerySet(self.model)
        #     print('qs_public', qs_public)
        # qs = qs.union(qs_public)
        # print('AQUI', qs)
        return qs

    # def all(self):
    #     print('all')
    #     return super().all()



# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
    # objects = CategoryManager()

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        schema_name = get_current_schema()
        if schema_name != 'public':
            raise ValidationError('Somente o admin pode deletar essa categoria')
        print('TESTE')
        super().delete(*args, **kwargs)
