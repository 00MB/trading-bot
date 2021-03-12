import requests

r = requests.get('https://finnhub.io/api/v1/')

print(r.json())