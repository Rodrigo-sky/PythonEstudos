from typing import final
import requests
import csv
import datetime

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = requests.get(url)
raw_data = resp.json()
final_data = []
for obs in raw_data:
   final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date'][:10]])

final_data.insert(0, ['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'data'])

with open('Aleatorio/projeto_covid.csv', 'w') as arquivo:
   escritor = csv.writer(arquivo)
   escritor.writerows(final_data)

for i in range(1, len(final_data)):
   final_data[i][4] = datetime.datetime.strptime(final_data[i][4], '%Y-%m-%d')
print(final_data)