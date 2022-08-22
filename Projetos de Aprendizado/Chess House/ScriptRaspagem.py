# Importação das bibliotecas

from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame


url = 'https://www.houseofchess.com/wood-chess-pieces.html'

cabecalho = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

pagina = get(url, headers = cabecalho)

sopa = BeautifulSoup(pagina.text, 'html.parser')

tag = sopa.find(name = 'div', class_='item_sel_wrapper')

#----------------------------------------------------------------------------------------

ListaCodigos = []

for subtag in tag.find_all(name = 'div', class_ = 'item_sel_outer_mid_desc_code'):
    ListaCodigos.append(subtag.string)

ListaNomes = []

for subtag in tag.find_all(name = 'div', class_ = "item_sel_outer_mid_desc_title"):
    ListaNomes.append(subtag.find(name='a').string)

ListaPrecos = []

for subtag in tag.find_all(name='span', class_='sale_price'):
    ListaPrecos.append(subtag.string)

#----------------------------------------------------------------------------------------

dicionario = {'Código':ListaCodigos, 'Nome':ListaNomes, 'Preço':ListaPrecos}

df = DataFrame(dicionario)
