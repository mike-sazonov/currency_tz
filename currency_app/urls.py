from django.urls import path
from . import views

urlpatterns = [
    path('get-current-usd/', views.CurrencyList.as_view()),
]