import re

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = "https://www.olx.pl/oferta/nowe-dwupokojowe-mieszkanie-na-mokotowie-zamykane-na-klucz-pokoje-CID3-IDwRpmd.html#337ce932e7;promoted"
    r = requests.get(url, stream=True)
    soup = BeautifulSoup(r.content, "html.parser")

    print soup.title
    print soup.findAll("table", {"class": "details"})