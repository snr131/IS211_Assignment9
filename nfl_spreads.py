import requests
from bs4 import BeautifulSoup

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'

def get_spread(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='html5lib')
    nestedtables = soup.table.find_all('table')
    nestedtable = nestedtables[13]
    trs = nestedtable.find_all('tr')
    spreadStats = trs[31:47]
    for stat in spreadStats:
        gameinfo = stat.find_all('td')
        date_and_time = gameinfo[0].text
        favorite = gameinfo[1].text
        spread = gameinfo[2].text
        underdog = gameinfo[3].text
        print('''
        Date & Time: {}
        Favorite: {}
        Spread: {}
        Underdog: {}'''.format(date_and_time, favorite, spread, underdog))

if __name__ == "__main__":
    get_spread(url)
