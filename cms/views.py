from itertools import chain

from django_tenants.utils import schema_context

from cms.models import Category
from customers.utils import get_current_schema
from education.models import School
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


    def get_queryset(self):
        lista = []
        queryset = super().get_queryset()
        schema = get_current_schema()
        lista.extend(list(queryset))
        print('---------')
        print('queryset', queryset)
        if schema != 'public':
            with schema_context('public'):
                qs_public = super().get_queryset()
                print('qs_public', qs_public)
                # queryset = list(chain(queryset, qs_public))
                lista.extend(list(qs_public))
        print('queryset', queryset)
        return lista

    #
    # def get_queryset(self):
    #     lista = []
    #     queryset = super().get_queryset()
    #     print(queryset)
    #     schema = get_current_schema()
    #     lista.extend(list(queryset))
    #     if schema != 'public':
    #         with schema_context('public'):
    #             qs_public = super().get_queryset()
    #             lista.extend(list(qs_public))
    #             # queryset.union(qs_public)
    #     print(lista)
    #     return lista