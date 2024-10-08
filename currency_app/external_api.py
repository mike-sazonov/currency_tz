import requests
from datetime import datetime, timezone

from .models import CurrencyModel

api_route = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_currency():
    last_obj = CurrencyModel.objects.order_by('-create')[0]
    if (datetime.now(timezone.utc) - last_obj.create).seconds < 10:  # разница создания последней записи и текущего времени
        return None
    else:
        response = requests.get(api_route)
        return response.json()['Valute']['USD']['Value']
