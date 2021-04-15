import requests
from bs4 import BeautifulSoup


url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/?sortcol=td&sortdir=descending'


def get_stats(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='html5lib')
    table = soup.table
    players = table.find_all('tr', limit=21)[1:]
    for player in players:
        name = player.find(attrs={'class': "CellPlayerName--long"}).a.text.strip()
        position = player.find(attrs={'class': "CellPlayerName-position"}).text.strip()
        team = player.find(attrs={'class': "CellPlayerName-team"}).text.strip()
        stats = player.find_all(attrs={'class': "TableBase-bodyTd TableBase-bodyTd--number"})
        touchdowns = stats[7].text.strip()
        print('''
        Player: {}  
        Position: {}
        Team: {}
        Passing Touchdowns: {}'''.format(name, position, team, touchdowns))


if __name__ == "__main__":
    get_stats(url)
