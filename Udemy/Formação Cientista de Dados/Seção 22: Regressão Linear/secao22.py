from pandas import read_csv
from scipy.stats import linregress
from pylab import plot, scatter, show, legend
from sklearn.linear_model import LinearRegression


# O dado tem duas colunas:
# - FrqAnual: Taxa Anual
# - CusInic: Investimento Inicial
#
# Tarefa:
# - Criar um modelo de regressão linear para prever qual será o investimento inicial necessário de uma franquia a partir
# da taxa anual cobrada pelo franqueador

# Do enunciado temos então que
# X = Taxa Anual
# Y = Investimento Inicial

# Obs: HÁ UM PONTO MUITO FORA DA CURVA


df = read_csv('slr12.csv', sep = ';')

x = df['FrqAnual'].to_numpy()
y = df['CusInic'].to_numpy()

##################################################################################
# Usando o scipy

instancia = linregress(x,y)

inclinacao = instancia.slope
y0 = instancia.intercept

Y = inclinacao*x + y0

scatter(x,y)
plot(x,Y, label = 'Usando o scipy', color = 'orange')
legend()
show()

##################################################################################
# Usando o sklearn

X = x.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(X,y)

scatter(X,y)
plot(X, modelo.predict(X), label = 'Usando o sklearn', color = 'orange')
legend()
show()
