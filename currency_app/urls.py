from django.urls import path
from . import views

urlpatterns = [
    path('', views.CurrencyList.as_view()),
]