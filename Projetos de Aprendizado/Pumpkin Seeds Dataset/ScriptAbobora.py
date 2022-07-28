#------------------------------------------------------------------------------
# IMPORTANDO BIBLIOTECAS

from pandas import read_excel

from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix, accuracy_score

#------------------------------------------------------------------------------
# DADOS INICIAIS

df = read_excel('Pumpkin_Seeds_Dataset.xlsx')

#------------------------------------------------------------------------------
# TRATAMENTO DE DADOS

df[ df.duplicated() ]

for i in df.columns:
    valor = int(df[i].isnull().sum())
    if valor > 0:
        print(i)

#------------------------------------------------------------------------------
# DIVISÃO ATRIBUTOS-CLASSE

x = df.iloc[:,0:12].values

y = df.iloc[:,12].values


#------------------------------------------------------------------------------
# CODIFICAÇÃO DE CATEGORIA
# NÃO ERA PRECISO CODIFICAR A CLASSE, POIS O SVM PRECISA APENAS QUE OS ATRIBUTOS SEJAM CODIFICADOS.
# (POR ISSO QUE ESTOU DEIXANDO COMENTADO AQUI)

# from sklearn.preprocessing import LabelEncoder
#
# codificador = LabelEncoder()
#
# y = codificador.fit_transform(y)

#------------------------------------------------------------------------------
# PARTICIONAMENTO DOS DADOS (treino e teste)

xTreino, xTeste, yTreino, yTeste = train_test_split(x,y,
                                                    test_size = 0.3,
                                                    random_state = 0)

#------------------------------------------------------------------------------
# IMPLEMENTAÇÃO DO SVM

svm = SVC()

svm.fit(xTreino, yTreino)

previsao = svm.predict(xTeste)

#-------------------------------------------------------------------------------
# PRECISÃO DO MODELO

matriz = confusion_matrix(previsao,yTeste)

print(matriz)

taxa = accuracy_score(previsao,yTeste)

print(taxa)
