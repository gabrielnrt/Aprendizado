# Parâmetros:
# - Aparência: sol, nublado, chuva
# - Temperatura: -130 a 130 F
# - Umidade: 0 a 100
# - Jogar: sim/nao

###################################################################
## Coisas que estão ruins:

# Na coluna 'Aparencia':
# - Há um elemento 'menos', fora do domínio 

# Na coluna 'Temperatura':
# - Há apenas um elemento fora do domínio, que é 1220 ºF

# Na coluna 'Umidade':
# - Há um elemento com NaN
# - Há um elemento fora do domínio, que é 200

from pandas import read_csv
