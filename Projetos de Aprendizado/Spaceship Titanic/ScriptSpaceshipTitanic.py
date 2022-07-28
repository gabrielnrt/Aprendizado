#-------------------------------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS

from pandas import read_csv, DataFrame

from statistics import mode

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

from numpy import concatenate

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB


#----------------------------------------------------------------------------
# LEITURA DOS DADOS

df = read_csv('train.csv')

#-----------------------------------------------------------------------------
# TRATAMENTO DOS DADOS

# TIRANDO COLUNAS
colunas = ['PassengerId', 'Cabin', 'Name']

df.drop(columns = colunas,
        inplace = True)

# CRIANDO UMA COLUNA DE GASTOS TOTAIS
df['GastoTotal'] = df['RoomService'] + df['FoodCourt'] + df['ShoppingMall'] + df['Spa'] + df['VRDeck']


colunas2 = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']

df.drop(columns = colunas2,
        inplace = True)


# PREENCHENDO CÉLULAS VAZIAS

PlanetaModa = mode(df['HomePlanet'])
df['HomePlanet'].fillna(value = PlanetaModa,
                        inplace = True)


ModaCryoSleep = mode(df['CryoSleep'])
df['CryoSleep'].fillna(value = ModaCryoSleep,
                       inplace = True)


DestinoModa = mode(df['Destination'])
df['Destination'].fillna(value = DestinoModa,
                         inplace = True)


MediaIdade = df['Age'].mean()
df['Age'].fillna(value = MediaIdade,
                 inplace = True)


VIPmoda = mode(df['VIP'])
df['VIP'].fillna(value = VIPmoda,
                 inplace = True)


GastoTotalMedio = df['GastoTotal'].mean()
df['GastoTotal'].fillna(value = GastoTotalMedio,
                        inplace = True)

#-----------------------------------------------------------------------------
# TROCANDO A ORDEM DAS COLUNAS
cols = ['HomePlanet', 'CryoSleep', 'Destination', 'Age', 'VIP', 'GastoTotal', 'Transported']

df = df[cols]

#------------------------------------------------------------------------------
# CODIFICAÇÃO DE CATEGORIAS (PARTE 1)

CodificadorPlaneta = OneHotEncoder(sparse = False,
                                    drop = 'first')

CodificadorDestino = OneHotEncoder(sparse = False,
                                    drop = 'first')

ArrayPlaneta = CodificadorPlaneta.fit_transform(df[['HomePlanet']])

ArrayDestino = CodificadorDestino.fit_transform(df[['Destination']])


arraytotal = concatenate((ArrayPlaneta, ArrayDestino),
                         axis = 1)

dfArraytotal = DataFrame(arraytotal)

df = df.join(dfArraytotal)

df.drop(columns = ['HomePlanet', 'Destination'],
        inplace = True)

#------------------------------------------------------------------------------
# MUDANDO A ORDEM DAS COLUNAS DE NOVO

df = df[['CryoSleep', 'Age', 'VIP', 'GastoTotal', 0, 1, 2, 3, 'Transported']]

#-----------------------------------------------------------------------------
# DIVIDINDO ATRIBUTOS E CLASSE

atributos = df.iloc[:,0:8].values

classe = df.iloc[:,8].values

#------------------------------------------------------------------------------
# CODIFICAÇÃO DE CATEGORIAS (PARTE 2)

LabelCry = LabelEncoder()

LabelVIP = LabelEncoder()

atributos[:,0] = LabelCry.fit_transform(atributos[:,0])

atributos[:,2] = LabelVIP.fit_transform(atributos[:,2])

#------------------------------------------------------------------------------
# PARTICIONAMENTO DOS DADOS

xTreino, xTeste, yTreino, yTeste = train_test_split(atributos, classe,
                                                    test_size = 0.3,
                                                    random_state = 0)

#------------------------------------------------------------------------------
# IMPLEMENTAÇÃO DO MODELO DE NAIVE-BAYES

modelo = GaussianNB()

modelo.fit(xTreino, yTreino)

previsao = modelo.predict(xTeste)

#------------------------------------------------------------------------------
# PRECISÃO DO MODELO

# from sklearn.metrics import confusion_matrix, accuracy_score
#
# matriz = confusion_matrix(previsao, yTeste)
#
# matriz
#
# TaxaAcerto = accuracy_score(previsao, yTeste)
#
# TaxaAcerto

#------------------------------------------------------------------------------
# APLICAÇÃO DO MODELO

df2 = read_csv('test.csv')

df2.drop(columns = colunas,
        inplace = True)

df2['GastoTotal'] = df2['RoomService'] + df2['FoodCourt'] + df2['ShoppingMall'] + df2['Spa'] + df2['VRDeck']

df2.drop(columns = colunas2,
        inplace = True)

PlanetaModa2 = mode(df2['HomePlanet'])
df2['HomePlanet'].fillna(value = PlanetaModa2,
                        inplace = True)


ModaCryoSleep2 = mode(df2['CryoSleep'])
df2['CryoSleep'].fillna(value = ModaCryoSleep2,
                       inplace = True)


DestinoModa2 = mode(df2['Destination'])
df2['Destination'].fillna(value = DestinoModa2,
                         inplace = True)


MediaIdade2 = df2['Age'].mean()
df2['Age'].fillna(value = MediaIdade2,
                 inplace = True)


VIPmoda2 = mode(df2['VIP'])
df2['VIP'].fillna(value = VIPmoda2,
                 inplace = True)


GastoTotalMedio2 = df2['GastoTotal'].mean()
df2['GastoTotal'].fillna(value = GastoTotalMedio2,
                        inplace = True)

cols2 = ['HomePlanet', 'CryoSleep', 'Destination', 'Age', 'VIP', 'GastoTotal']

df2 = df2[cols2]

CodificadorPlaneta2 = OneHotEncoder(sparse = False,
                                    drop = 'first')

CodificadorDestino2 = OneHotEncoder(sparse = False,
                                    drop = 'first')

ArrayPlaneta2 = CodificadorPlaneta2.fit_transform(df2[['HomePlanet']])

ArrayDestino2 = CodificadorDestino2.fit_transform(df2[['Destination']])

arraytotal2 = concatenate((ArrayPlaneta2, ArrayDestino2),
                         axis = 1)

dfArraytotal2 = DataFrame(arraytotal2)

df2 = df2.join(dfArraytotal2)

df2.drop(columns = ['HomePlanet', 'Destination'],
        inplace = True)


df2 = df2[['CryoSleep', 'Age', 'VIP', 'GastoTotal', 0, 1, 2, 3]]


atributos2 = df2.iloc[:,0:8].values


LabelCry2 = LabelEncoder()

LabelVIP2 = LabelEncoder()

atributos2[:,0] = LabelCry2.fit_transform(atributos2[:,0])

atributos2[:,2] = LabelVIP2.fit_transform(atributos2[:,2])

previsao2 = modelo.predict(atributos2)


#------------------------------------------------------------------------------
# GERANDO ARQUIVO FINAL

IdPassageiros = read_csv('test.csv',
                          usecols = ['PassengerId'])

dicionario = {'PassengerId': IdPassageiros['PassengerId'],
              'Transported': previsao2}

resultado = DataFrame(dicionario)

resultado.to_csv('RespostaSpaceshipTitanic.csv',
                  index = False)
