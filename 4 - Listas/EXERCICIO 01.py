"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
"""
lista = []

for i in range(1, 6, 1):
    while True:
        try:
            valor = int(input('Entre com um número inteiro: '))
            if valor >= 0:
                lista.append(valor)
                break
            else:
                print('Você entrou com um valor negativo, tente novamente.')
        except ValueError:
            print('Você digitou um valor inválido, tente novamente.')

print(f'\nOs números inteiros inseridos foram: {lista}')
