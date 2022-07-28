#-----------------------------------------------------------------------------
# Importação das bibliotecas

from pandas import read_csv, DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

#----------------------------------------------------------------------------
# Leitura dos dados de treino

df = read_csv('train.csv')


#---------------------------------------------------------------------------
# Tirando algumas colunas e movendo a classe (Survived) pro fim da tabela

df2 = df.pop('Survived')

df['Survived'] = df2


ColunasExcluidas = ['Name', 'Ticket', 'Cabin']

df.drop(columns = ColunasExcluidas,
        inplace = True)
#------------------------------------------------------
# Células Nulas

IdadeMedia = df['Age'].mean()
df['Age'].fillna(value = IdadeMedia, inplace = True)

moda = df['Embarked'].mode()
df['Embarked'].fillna(value = 'S', inplace = True)
# Obs: a moda é 'S', e coloquei direto pois se coloco
# value=moda o método não realiza a substituição.

#-----------------------------------------------------------
# Codificação das categorias

atributos = df.iloc[:,0:8].values
classe = df.iloc[:,8].values

codificador1 = LabelEncoder()
codificador2 = LabelEncoder()

atributos[:,2] = codificador1.fit_transform(atributos[:,2])
atributos[:,7] = codificador2.fit_transform(atributos[:,7])

#--------------------------------------------------------------
# Particionamento dos dados

xTreino, xTeste, yTreino, yTeste = train_test_split(atributos, classe,
                                                    test_size = 0.3,
                                                    random_state = 0)

#-------------------------------------------------------------------------------
# Criação da árvore de decisão

arvore = DecisionTreeClassifier()

arvore.fit(xTreino, yTreino)

previsoes = arvore.predict(xTeste)

#------------------------------------------------------------------------------
# Avaliação da acurácia do modelo

# matriz = confusion_matrix(previsoes, yTeste)
#
# TaxaAcerto = accuracy_score(previsoes,yTeste)

#-------------------------------------------------------------------------------
# Implementação do modelo com os dados de teste

df2 = read_csv('test.csv')

df2.drop(columns = ColunasExcluidas,
        inplace = True)

MediaDasIdades = df2['Age'].mean()
df2['Age'].fillna(value = MediaDasIdades, inplace = True)

MediaFare = df2['Fare'].mean()
df2['Fare'].fillna(value = MediaFare, inplace = True)


X = df2.iloc[:,0:8].values

codificador3 = LabelEncoder()
codificador4 = LabelEncoder()

X[:,2] = codificador3.fit_transform(X[:,2])
X[:,7] = codificador4.fit_transform(X[:,7])

Y = arvore.predict(X)

dicionario = {'PassengerId': X[:,0], 'Survived': Y}

RespostaObtida = DataFrame(dicionario)

RespostaObtida.to_csv('RespostaTitanic.csv', index = False)
