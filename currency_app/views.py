from django.http import HttpResponse

from .external_api import get_currency
from rest_framework.generics import ListAPIView
from .serializers import CurrencyModelSerializer
from .models import CurrencyModel


class CurrencyList(ListAPIView):
    serializer_class = CurrencyModelSerializer
    queryset = CurrencyModel.objects.order_by('-create')[:11]   # список записей из бд, отсортированный по времени создания

    def get(self, request, *args, **kwargs):
        try:
            CurrencyModel.objects.create(value=get_currency())  # создание новой записи в бд с данными из api
        except Exception:
            return HttpResponse(
                'Exception: the time between requests should be 10 seconds'
            )  # вызов исключения, если между запросами меньше 10 секунд
        return super().get(self)
