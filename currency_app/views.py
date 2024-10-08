from django.http import HttpResponse

from django.shortcuts import render
from django.views.debug import ExceptionReporter

from .api import get_currency
from rest_framework.generics import ListAPIView
from .serializers import CurrencyModelSerializer
from .models import CurrencyModel


class CurrencyList(ListAPIView):
    serializer_class = CurrencyModelSerializer
    queryset = CurrencyModel.objects.order_by('-create')[:10]

    def get(self, request, *args, **kwargs):
        try:
            CurrencyModel.objects.create(value=get_currency())
        except Exception:
            return HttpResponse(
                'Exception: the time between requests should be 10 seconds'
            )  # вызов исключения, если между запросами меньше 10 секунд
        return super().get(self)