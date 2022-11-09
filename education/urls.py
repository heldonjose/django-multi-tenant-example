from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.SchoolsList.as_view()),
]
