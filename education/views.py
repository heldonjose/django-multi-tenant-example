from education.models import School
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolsList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]
