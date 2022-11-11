# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django_tenants.management.commands import BaseTenantCommand
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

    # tenant = Client(schema_name='tenant1',
    #                 name='HELDON JOSE',
    #                 paid_until='2014-12-05',
    #                 on_trial=True)
    # tenant.save()  # migrate_schemas automatically called, your tenant is ready to be used!
    #
    # # Add one or more domains for the tenant
    # domain = Domain()
    # domain.domain = 'localhost'  # don't add your port or www here!
    # domain.tenant = tenant
    # domain.is_primary = True
    # domain.save()


# manage.py tenant_command do_foo --schema=tenant1
class Command(BaseCommand):
# class Command(BaseTenantCommand):
    help = 'Update performance cycles status'
    # COMMAND_NAME = 'teste1'
    # create_schemas()

    #
    def handle(self, **options):
        print(Category.objects.all())
        with schema_context('tenant1'):
            print('asdasd')
            print(Category.objects.all())
        print(Category.objects.all())




# 1 - Fazer o rebase (duas sp1 ) para a main.
# 2 - Fazer o rebase para o django40;
# 3 - Fazer a limpeza dos migrates para criação de uma base limpa;
# 4 - Colocar multitanent - CM - Public e Portal private;
# 5 - Trazer a parte de Autenticação (doc) - URL e View  - JWT para o app core (Criar se não existir)
# 6 - Validações para os tenants não alterar (Criar, deletar ou editar) os dados dos esquemas public (Perguntar a Alessandro)

#teste
 # - Sobrescrever o sampledb para deletar todos as chaves que não serão mais utilizadas. e adcoinar o tenant e dominios
 # - Trazer os teste de portal e cms para sobrecreve-los utilizando mais de 1 tenant (public + 3)