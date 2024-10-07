from requests import Response

from .api import get_currency
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CurrencyModelSerializer
from .models import CurrencyModel

class CurrencyList(APIView):
    serializer_class = CurrencyModelSerializer
    cur_value = get_currency()

    def get(self, request, *args, **kwargs):
        api_request = CurrencyModel.objects.create(value=self.cur_value)
        serializer = CurrencyModelSerializer(api_request)
        return Response(serializer.data)
