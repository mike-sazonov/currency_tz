import requests

def get_currency():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return response.json()['Valute']['USD']['Value']
