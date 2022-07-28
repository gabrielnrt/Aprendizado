#-----------------------------------------------------------------------------
# IMPORTANDO AS BIBLIOTECAS

from pandas import read_csv, DataFrame
from pylab import plot, scatter, show, xlabel, ylabel, title
from scipy.stats import linregress


#-----------------------------------------------------------------------------
# LEITURA DOS DADOS

caracteristica = 'GrLivArea'

colunas = [caracteristica, 'SalePrice']

df = read_csv('train.csv',
               usecols = colunas)

df

#-----------------------------------------------------------------------------
# PARTIÇÃO DOS DADOS

X = df[caracteristica].to_numpy()

y = df['SalePrice'].to_numpy()

X

#-----------------------------------------------------------------------------
# VISUALIZAÇÃO DOS DADOS

scatter(X,y)
xlabel('Área da garagem')
ylabel('Preço do imóvel')
show()


#-----------------------------------------------------------------------------
# REGRESSÃO LINEAR

instancia = linregress(X,y)

y0 = instancia.intercept

inclinacao = instancia.slope

y_modelo = inclinacao*X + y0

plot(X, y_modelo, color = 'green')
scatter(X,y)
xlabel('Área da garagem')
ylabel('Preço do imóvel')
show()

#-----------------------------------------------------------------------------
# IMPLEMENTAÇÃO DO MODELO

df2 = read_csv('test.csv',
                usecols = ['Id',caracteristica])

df2

x = df2[caracteristica].to_numpy()

previsao = inclinacao*x + y0

plot(X, y_modelo, color = 'green')
scatter(x,previsao)
xlabel('Área da garagem')
ylabel('Preço do imóvel')
show()

dicionario = {'Id': df2['Id'], 'SalePrice': previsao}

resposta = DataFrame(dicionario)

resposta

resposta.to_csv('HousePricesResposta.csv',
                 index = False)
