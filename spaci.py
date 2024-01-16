import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API da OpenWeatherMap
api_key = '2a980c9e9a9bca47feca1752b1474cba'

# URL da API da OpenWeatherMap para obter a previsão do tempo por cidade
url = 'http://api.openweathermap.org/data/2.5/weather'

# Parâmetros da consulta (cidade, chave da API, unidade de medida)
params = {'q': 'London,uk', 'appid': api_key, 'units': 'metric'}

# Faz a chamada à API
response = requests.get(url, params=params)

# Verifica se a chamada foi bem-sucedida (código de resposta 200)
if response.status_code == 200:
    # Converte a resposta para formato JSON
    data = response.json()
    # Exibe os dados
    print(data)
else:
    print(f'Erro na chamada à API: {response.status_code}')
    print(response.text)