from cms.models import Category
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
