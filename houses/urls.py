from django.urls import path
from . import views

urlpatterns = [
    path('houses/', views.HouseList.as_view()),
]
