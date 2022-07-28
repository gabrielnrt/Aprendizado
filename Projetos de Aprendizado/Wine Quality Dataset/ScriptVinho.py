#----------------------------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS

from pandas import read_csv

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


#-----------------------------------------------------------------------------
# DADOS INICIAIS

df = read_csv('WineQT.csv')

#-----------------------------------------------------------------------------
# TRATAMENTO DE DADOS

# df[ df.duplicated() ]
#
# df[ df['fixed acidity'].isnull() ]
#
# df[ df['volatile acidity'].isnull() ]
#
# df[ df['citric acid'].isnull() ]
#
# df[ df['residual sugar'].isnull() ]
#
# df[ df['chlorides'].isnull() ]
#
# df[ df['free sulfur dioxide'].isnull() ]
#
# df[ df['total sulfur dioxide'].isnull() ]
#
# df[ df['density'].isnull() ]
#
# df[ df['pH'].isnull() ]
#
# df[ df['sulphates'].isnull() ]
#
# df[ df['alcohol'].isnull() ]
#
# df[ df['quality'].isnull() ]
#
# df[ df['Id'].isnull() ]

#-----------------------------------------------------------------------------
# DIVISÃO DE ATRIBUTOS E CLASSE

atributos = df[ ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'] ]

classe = df[['quality']]

#------------------------------------------------------------------------------
# PARTICIONAMENTO DE TREINO E TESTE


x = atributos.values
y = classe.iloc[:,0].values

xTreino, xTeste, yTreino, yTeste = train_test_split(x,y,
                                                    test_size = 0.3,
                                                    random_state = 0)

#------------------------------------------------------------------------------
# IMPLEMENTAÇÃO DA FLORESTA ALEATÓRIA


floresta = RandomForestClassifier(n_estimators = 100)

floresta.fit(xTreino,yTreino)

previsao = floresta.predict(xTeste)

#------------------------------------------------------------------------------
# PRECISÃO DO MODELO


taxa = accuracy_score(previsao,yTeste)
