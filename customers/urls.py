from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.ClientList.as_view()),
]
