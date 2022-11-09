from django.shortcuts import render
from houses.models import House
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class HouseList(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [AllowAny]
