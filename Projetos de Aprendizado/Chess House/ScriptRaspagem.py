# Importação das bibliotecas

from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame
from re import findall

url = 'https://www.houseofchess.com/wood-chess-pieces.html'

cabecalho = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

pagina = get(url, headers = cabecalho)

sopa = BeautifulSoup(pagina.text, 'html.parser')

tag = sopa.find(name = 'div', class_='item_sel_wrapper')

#----------------------------------------------------------------------------------------

ListaCodigos = []
ListaNomes = []
ListaPrecos = []
ListaAlturas = []
ListaMateriais = []


for subtag in tag.find_all(name = 'div', class_ = 'item_sel_outer'):

    codigo = subtag.find(name = 'div', class_ = 'item_sel_outer_mid_desc_code').string
    ListaCodigos.append(codigo)

    nome = subtag.find(name = 'div', class_ = "item_sel_outer_mid_desc_title").find(name = 'a').string
    ListaNomes.append(nome)

    preco = subtag.find(name='span', class_='sale_price').string
    ListaPrecos.append(preco)

    altura = subtag.find(name = 'strong', style = '').string
    ListaAlturas.append(altura)

    material = subtag.find(name = 'strong', style = 'color:green').string
    ListaMateriais.append(material)

#----------------------------------------------------------------------------------------

dicionario = {'Código':ListaCodigos, 'Nome':ListaNomes, 'Altura (Polegadas)':ListaAlturas, 'Material':ListaMateriais,'Preço (USD)':ListaPrecos}

df = DataFrame(dicionario)

df['Código'] = df['Código'].apply(lambda texto:texto.replace('Item# ', '') )

df['Preço (USD)'] = df['Preço (USD)'].apply(lambda texto:texto.replace('Sale Price: $', ''))

df['Altura (Polegadas)'] = df['Altura (Polegadas)'].apply(lambda texto: findall('\d{1}\.?\d*', texto)[0] )

#-----------------------------------------------------------------------------------------------------
# Conversão de tipagem

df['Altura (Polegadas)'] = df['Altura (Polegadas)'].astype(float)

df['Preço (USD)'] = df['Preço (USD)'].astype(float)


print(df.head())
