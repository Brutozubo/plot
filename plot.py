import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
from datetime import datetime

url = 'https://mfd.ru/currency/?currency=USD'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
graph = soup.find('table', attrs={"class":{"mfd-table mfd-currency-table"}})
rows = graph.find_all('tr')

dates = []
prices = []

for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
        dates.append(datetime.strptime(columns[0].text[2:], '%d.%m.%Y'))
        prices.append(float(columns[1].text))

pyplot.plot(dates, prices)
pyplot.show()