from django.shortcuts import render


from customers.models import Client
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
