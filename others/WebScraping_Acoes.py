# pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

pg = requests.get('https://fundamentus.com.br/fii_resultado.php', headers = headers)

soup = BeautifulSoup(pg.text, 'html.parser')

dice = soup.find("table", {"id": "tabelaResultado"}).find('tbody').find_all('tr')

for results in dice:
    dice_actions = results.find_all("td")
    print(
        f"[{dice_actions[0].text}]\n"
        f"[\tCotacao: {dice_actions[2].text}]\n"
        f"[\tSetor: {dice_actions[1].text}]\n"
        f"[\tDY(%): {dice_actions[4].text}]\n"
        f"[\tP/VP: {dice_actions[5].text}]\n"
    )