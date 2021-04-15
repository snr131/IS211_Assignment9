import requests
from bs4 import BeautifulSoup

url = 'https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history'

def get_aapl_byyear(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='lxml')
    table = soup.table
    print(table.find('th').text.strip())
    trs = table.find_all('tr')
    for tr in trs[2:]:
        byyear = tr.find_all('td')
        year = byyear[0].text
        yearClose = byyear[5].text
        print('''
        Year: {}
        Year Close: {}'''.format(year, yearClose))

if __name__ == "__main__":
    get_aapl_byyear(url)
