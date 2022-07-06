"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
contador = 0
maior = 0
menor = 0
fim_de_programa = False

while fim_de_programa is False:
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Digite um valor válido! ')

    if numero == -1:
        fim_de_programa = True
    if numero >= 0:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'MAIOR = {maior}\nMENOR = {menor} \nSOMA: {maior + menor}')
