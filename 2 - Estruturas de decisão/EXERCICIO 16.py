"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
print('FUNÇÃO DE 2° GRAU - DIGITE OS VALORES DE A , B e C PARA ENCONTRAR AS RAÍZES DA EQUAÇÃO')
import math

ah = float(input('INSIRA O VALOR DE A: '))

if ah != 0:
    be, ce = float(input('INSIRA O VALOR DE B: ')), float(input('INSIRA O VALOR DE C: '))
    delta = pow(be, 2) - (4 * ah * ce)

    if delta < 0:
        print('\nA equação não possui raízes reais, programa encerrado!')
    elif delta == 0:
        raiz1 = (be * -1) / (2 * ah)
        print(f'\nA equação possui apenas uma raiz real, {raiz1}')
    else:
        raiz1 = ((be * -1) + math.sqrt(delta)) / (2 * ah)
        raiz2 = ((be * -1) - math.sqrt(delta)) / (2 * ah)
        print(f'\nA equação possui duas raízes reais: {raiz1} e {raiz2}')

else:
    print('\nA variável A é igual a zero e não satisfaz uma equação do segundo grau!')
