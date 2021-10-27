# Linha de teste
##################################################################
# Parâmetros:
# - Aparência: sol, nublado, chuva
# - Temperatura: -130 a 130 F
# - Umidade: 0 a 100
# - Jogar: sim/nao

###################################################################
## Coisas que estão ruins:

# Na coluna 'Aparencia':
# - Há um elemento 'menos', fora do domínio
# - Os elementos mais frequentes são 'sol' e 'chuva'

# Na coluna 'Temperatura':
# - Há apenas um elemento fora do domínio, que é 1220 ºF

# Na coluna 'Umidade':
# - Há um elemento NaN
# - Há um elemento fora do domínio, que é 200

# Na coluna 'Vento':
# - Há um elemento NaN
# - O elemento mais comum (moda) é 'FALSO'

###################################################################

from pandas import read_csv
from statistics import mean, median


df = read_csv('tempo.csv', delimiter = ';')

# Consertando a coluna 'Aparencia'
ModaAparencia = 'sol'
df.loc[ df['Aparencia']=='menos' ,'Aparencia'] = ModaAparencia
# Poderia substituir por 'chuva' também

# Consertando a coluna 'Temperatura' (substituir o valor estranho pela média)
TempMedia = mean(df['Temperatura'])
df.loc[ df['Temperatura'] > 130 ,'Temperatura'] = TempMedia

# Consertando a coluna 'Umidade'
# - Vou substituir o NaN pela mediana ao invés da média porque a função média vai me retornar um 'NaN'
UmidadeMediana = median(df['Umidade'])
df['Umidade'].fillna(UmidadeMediana, inplace = True)

# - Agora que o NaN já foi preenchido, vou calcular a média e usá-la para substituir o valor fora do domínio
UmidadeMedia = mean(df['Umidade'])
df.loc[df['Umidade'] > 100, 'Umidade'] = UmidadeMedia

# Consertando a coluna 'Vento'
ModaVento = 'FALSO'
df['Vento'].fillna(ModaVento, inplace = True)

print(df)
