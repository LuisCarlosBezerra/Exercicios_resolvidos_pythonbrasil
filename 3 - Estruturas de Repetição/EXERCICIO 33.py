"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
das temperaturas.
"""
from typing import Text

print('PROGRAMA DE VERIFICAÇÃO DE TEMPERATURAS - INSTITUTO DE METEOROLOGIA TABAJARA')
contador_temp = 0
acumulador_temp = 0
temp = 0

while True:
    try:
        temp = float(input('Entre com o valor da temperatura. Digite -999 para encerrar o programa '))
    except ValueError:
        print('Você digitou um valor inválido, tente novamente.')
    if (temp >= -50) and (temp <= 50):
        acumulador_temp += temp
        contador_temp += 1

        if contador_temp == 1:
            maior_temp = temp
            menor_temp = temp
        if contador_temp > 1:
            if temp <= menor_temp:
                menor_temp = temp
            if temp >= maior_temp:
                maior_temp = temp
    elif temp == -999:
        print('\nPROGRAMA ENCERRADO')
        break
    else:
        print('Você digitou um valor fora do intervalo válido, tente novamente. ')

print(
    f'A MENOR temperatura digitada foi: {menor_temp} ºC\nA MAIOR temperatura digitada foi: {maior_temp}'
    f' ºC\nA temperatura MÉDIA foi de {(acumulador_temp / contador_temp):.2f} ºC')
