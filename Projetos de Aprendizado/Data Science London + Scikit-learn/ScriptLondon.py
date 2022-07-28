#-----------------------------------------------------------------------------
# IMPORTANDO AS BIBLIOTECAS

from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


#-----------------------------------------------------------------------------
# LEITURA DOS DADOS DE TREINO

df = read_csv('train.csv',
               header = None)

classes = read_csv('trainLabels.csv',
                    header = None)

#----------------------------------------------------------------------------
# FATIAMENTO DOS DADOS DE TREINO

atributos = df.values

classe = classes.iloc[:,0].values

xTreino, xTeste, yTreino, yTeste = train_test_split(atributos, classe,
                                                    test_size = 0.3,
                                                    random_state = 0)

#----------------------------------------------------------------------------
# IMPLEMENTAÇÃO DO KNN

vizinhos = 3
knn = KNeighborsClassifier(n_neighbors = vizinhos)

knn.fit(xTreino, yTreino)

previsao = knn.predict(xTeste)

#----------------------------------------------------------------------------
# PRECISÃO DO MODELO

matriz = confusion_matrix(previsao, yTeste)

TaxaAcerto = accuracy_score(previsao,yTeste)

#-----------------------------------------------------------------------------
# APLICAÇÃO DO MODELO NOS DADOS DE TESTE

teste = read_csv('test.csv',
                  header = None)

ATRIBUTOS = teste.iloc[:,:].values

RESULTADOS = knn.predict(ATRIBUTOS)

indices = list(range(1,9001))

dicionario = {'Id': indices, 'Solution': RESULTADOS}

dados = DataFrame(dicionario)

dados.to_csv('SolucaoLondon.csv',
              index = False)
