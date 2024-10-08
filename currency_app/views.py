from .api import get_currency
from rest_framework.generics import ListAPIView
from .serializers import CurrencyModelSerializer
from .models import CurrencyModel

class CurrencyList(ListAPIView):
    serializer_class = CurrencyModelSerializer
    queryset = CurrencyModel.objects.order_by('-create')[:10]

    def get(self, request, *args, **kwargs):
        CurrencyModel.objects.create(value=get_currency())
        return super().get(self)