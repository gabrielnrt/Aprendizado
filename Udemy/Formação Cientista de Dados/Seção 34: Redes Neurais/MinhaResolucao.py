from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score


df = read_csv('soybean.csv')

#-----------------------------------------------------------------------------------
x = df.iloc[:,:35].values
y = df['class'].values

for i in range(35):
    codificador = LabelEncoder()
    x[:,i] = codificador.fit_transform(x[:,i])

instancia = LabelEncoder()
y = instancia.fit_transform(y)

XTreino, XTeste, YTreino, YTeste = train_test_split(x,y,
                                                   test_size = 0.3,
                                                   random_state = 0)

#----------------------------------------------------------------------------------

modelo = GaussianNB()

modelo.fit(XTreino,YTreino)

previsao = modelo.predict(XTeste)

confusao = confusion_matrix(previsao,YTeste)
print(confusao)

print(accuracy_score(previsao,YTeste))
